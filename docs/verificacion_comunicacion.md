
# Documentación: Proceso de Verificación de Comunicación con SIAT

## 1. Introducción

Este documento detalla el funcionamiento de la página "Verificador de Comunicación con SIAT" implementada en el archivo `pages/1_Verificar_comunicacion.py`. El propósito principal de esta página es permitir al usuario comprobar el estado de conectividad y la respuesta de los diversos servicios web SOAP proporcionados por el Servicio de Impuestos Nacionales (SIAT) de Bolivia, relacionados con el sistema de facturación electrónica.

## 2. Configuración Requerida

Para el correcto funcionamiento de esta página, es esencial configurar ciertas variables de entorno en un archivo `.env` ubicado en la raíz del proyecto. Estas variables son:

*   `API_KEY`: La clave de API proporcionada por el SIAT para la autenticación con sus servicios.
*   `WSDL_URL_CODIGOS`: URL del servicio WSDL para la obtención de códigos y catálogos.
*   `WSDL_URL_OPERACIONES`: URL del servicio WSDL para operaciones de facturación.
*   `WSDL_URL_SYNC`: URL del servicio WSDL para la sincronización de datos.
*   `WSDL_URL_AJUSTE`: URL del servicio WSDL para documentos de ajuste.
*   `WSDL_URL_FACTURACION`: URL del servicio WSDL para la facturación de compra y venta.

Si la `API_KEY` no está configurada, la página mostrará un error y no permitirá continuar. Si alguna de las URLs de los servicios no está definida, ese servicio específico no podrá ser verificado y se marcará como "No configurado" en la tabla de resultados.

## 3. Interfaz de Usuario y Flujo de Interacción

La página presenta la siguiente interfaz y flujo:

1.  **Título y Descripción**: Se muestra el título "Verificador de Comunicación con SIAT" y una breve descripción de su propósito.
2.  **Opciones de Verificación**:
    *   **Selección de Servicios**: Un selector múltiple (`st.multiselect`) permite al usuario elegir cuáles de los servicios configurados desea verificar. Por defecto, todos los servicios están seleccionados.
    *   **Botones de Acción**:
        *   `Verificar Todos`: Inicia la verificación de todos los servicios listados en la configuración.
        *   `Verificar Seleccionados`: Inicia la verificación únicamente de los servicios que el usuario haya marcado en el selector múltiple.
3.  **Estado de los Servicios**:
    *   **Barra de Progreso**: Al iniciar la verificación, una barra de progreso (`st.progress`) informa al usuario sobre el avance del proceso, mostrando cuántos servicios se han verificado del total.
    *   **Indicadores Individuales**: Durante la verificación de cada servicio, un placeholder (`st.empty`) muestra el estado en tiempo real de esa verificación específica (ej. "Verificando...", "OK", "TIMEOUT", "ERROR DE CONEXIÓN").
    *   **Tabla de Resultados**: Una vez completadas todas las verificaciones solicitadas, se presenta una tabla (`st.dataframe`) con los siguientes campos para cada servicio:
        *   `Servicio`: Nombre descriptivo del servicio.
        *   `Estado`: Indicador visual y textual del resultado ("✅ Operativo", "❌ Con problemas", "⚠️ No configurado").
        *   `Mensaje`: Detalles adicionales sobre el resultado, como el tiempo de respuesta, códigos de error del SIAT, o mensajes de error de conexión.
4.  **Mensaje General y Sugerencias**:
    *   Si todos los servicios verificados están operativos, se muestra un mensaje de éxito (`st.success`).
    *   Si alguno de los servicios presenta problemas o no está configurado, se muestra un mensaje de advertencia (`st.warning`) instando al usuario a revisar la tabla.
    *   Adicionalmente, si se detectan problemas, se muestra una sugerencia (`st.warning`) sobre la posibilidad de activar el modo de contingencia, indicando que esta opción se encuentra en otra sección de la aplicación.

## 4. Proceso Interno de Verificación (Función `verificar_servicio`)

Cada servicio es verificado individualmente por la función `verificar_servicio(url, nombre_servicio)`:

1.  **Registro (Logging)**: Se registra un mensaje `INFO` al iniciar la verificación del servicio.
2.  **Preparación de la Solicitud SOAP**:
    *   Se utiliza una plantilla XML predefinida para la operación `verificarComunicacion` del SIAT.
    *   Se configuran las cabeceras HTTP, incluyendo `Content-Type`, `SOAPAction` (vacía para este servicio) y la `apikey` obtenida de las variables de entorno.
3.  **Envío de la Solicitud**:
    *   Se realiza una petición HTTP `POST` al `url` del servicio utilizando la librería `requests`.
    *   Se establece un `timeout` de 10 segundos para la respuesta.
    *   Se registra un mensaje `DEBUG` con el código de estado HTTP de la respuesta.
4.  **Verificación de Respuesta HTTP**: Se utiliza `response.raise_for_status()` para asegurar que el código de estado HTTP sea exitoso (ej. 200 OK). Si no lo es, se lanza una excepción.
5.  **Cálculo del Tiempo de Respuesta**: Se mide el tiempo transcurrido desde el envío de la solicitud hasta la recepción de la respuesta.
6.  **Procesamiento de la Respuesta SOAP**:
    *   El contenido XML de la respuesta (`response.content`) se pasa a la función `parse_siat_response` del módulo `response_handler.py`.
    *   Esta función interpreta el XML y devuelve una tupla: `(success, response_data)`, donde `success` indica si el parseo fue exitoso y `response_data` es un diccionario con los datos extraídos (ej. `transaccion`, `codigoEstado`, `codigoDescripcion`, `error`).
7.  **Determinación del Estado del Servicio**:
    *   **Transacción Exitosa SIAT**: Si `parse_siat_response` fue exitoso y `response_data.get('transaccion', False)` es `True`, el servicio se considera "OK". Se actualiza el `status_placeholder` con un mensaje de éxito y se registra un `INFO` log.
    *   **Respuesta SIAT No Exitosa**: Si `parse_siat_response` fue exitoso pero la transacción SIAT no lo fue, se considera una advertencia. Se extraen el `codigoEstado` y `codigoDescripcion` del SIAT. Se actualiza el `status_placeholder` y se registra un `WARNING` log.
    *   **Error de Parseo**: Si `parse_siat_response` indica un error, se considera un fallo. Se actualiza el `status_placeholder` y se registra un `ERROR` log.
8.  **Manejo de Excepciones**:
    *   `requests.exceptions.Timeout`: Si la solicitud excede los 10 segundos, se actualiza el `status_placeholder` con "TIMEOUT" y se registra un `ERROR` log.
    *   `requests.exceptions.ConnectionError`: Si hay problemas para establecer conexión con el servidor (ej. no hay internet, el host no resuelve), se actualiza el `status_placeholder` con "ERROR DE CONEXIÓN" y se registra un `ERROR` log.
    *   `requests.exceptions.RequestException`: Captura cualquier otra excepción relacionada con la solicitud HTTP. Se actualiza el `status_placeholder` y se registra un `ERROR` log.
9.  **Retorno**: La función devuelve una tupla `(bool, str)` indicando el éxito general de la comunicación y un mensaje descriptivo.

## 5. Lógica Principal de la Página (Función `main`)

La función `main()` orquesta la página:

1.  **Verificación de `API_KEY`**: Comprueba si `API_KEY` está definida. Si no, muestra un error y termina la ejecución de la página.
2.  **Carga de Endpoints**: Lee las URLs de los servicios SIAT desde las variables de entorno y las almacena en un diccionario `endpoints`.
3.  **Renderizado de la UI**: Utiliza los componentes de Streamlit (`st.title`, `st.write`, `st.multiselect`, `st.button`, `st.columns`, `st.subheader`) para construir la interfaz.
4.  **Manejo de Acciones del Usuario**:
    *   Si se presiona "Verificar Todos" o "Verificar Seleccionados" (y hay servicios seleccionados):
        *   Determina la lista de `servicios_a_verificar`.
        *   Inicializa la barra de progreso.
        *   Itera sobre `servicios_a_verificar`:
            *   Si el servicio tiene una URL configurada, llama a `verificar_servicio`.
            *   Almacena el resultado (`Servicio`, `Estado`, `Mensaje`) en una lista `results`.
            *   Si el servicio no tiene URL configurada, lo marca como "No configurado".
            *   Actualiza la barra de progreso.
        *   Limpia la barra de progreso al finalizar.
5.  **Presentación de Resultados Consolidados**:
    *   Si la lista `results` no está vacía, la convierte en un DataFrame de Pandas y la muestra usando `st.dataframe`.
    *   Evalúa si `todos_operativos` son `True` y muestra el mensaje de éxito o advertencia correspondiente, incluyendo la sugerencia de contingencia.
    *   Si `results` está vacía (porque no se seleccionó ningún servicio o la lista estaba vacía inicialmente), muestra una advertencia.

## 6. Módulos Involucrados

*   **`streamlit`**: Framework principal para la creación de la interfaz de usuario web.
*   **`requests`**: Librería para realizar las peticiones HTTP a los servicios SOAP.
*   **`dotenv` (`python-dotenv`)**: Para cargar variables de entorno desde el archivo `.env`.
*   **`pandas`**: Para la creación y visualización de la tabla de resultados.
*   **`response_handler.py`**: Módulo personalizado que contiene la lógica `parse_siat_response` para interpretar las respuestas XML del SIAT.
*   **`logger_config.py`**: Módulo personalizado que configura y proporciona instancias del logger para el registro de eventos y errores.
