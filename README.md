# BACKSTAGE - SIAT

## Descripción

**BACKSTAGE - SIAT** es una aplicación desarrollada en Python con Streamlit diseñada para interactuar con los servicios web del SIAT (Servicio de Impuestos Nacionales de Bolivia). Actualmente, la funcionalidad principal implementada es la verificación de la comunicación con los diferentes endpoints del SIAT.

La aplicación facilita a los usuarios la comprobación del estado de los servicios de facturación electrónica, proporcionando una interfaz amigable y respuestas claras sobre la disponibilidad y el rendimiento de cada servicio.

## Características

*   **Verificación de Comunicación con SIAT**: Permite enviar solicitudes de prueba a los endpoints de:
    *   Facturación Códigos
    *   Facturación Operaciones
    *   Facturación Sincronización
    *   Documentos de Ajuste
    *   Facturación Compra-Venta
*   **Interfaz de Usuario Amigable**: Construida con Streamlit para una fácil interacción.
*   **Manejo de Respuestas**: Procesa y muestra las respuestas de los servicios SIAT.
*   **Configuración Flexible**: Utiliza variables de entorno para la gestión de API Keys y URLs de los servicios.
*   **Logging Detallado**: Registra las operaciones y errores para facilitar la depuración y el seguimiento.

## Prerrequisitos

*   Python 3.8 o superior
*   pip (manejador de paquetes de Python)
*   Un entorno virtual (recomendado)
*   Credenciales de API KEY para los servicios del SIAT.

## Configuración del Proyecto

1.  **Clonar el Repositorio (si aplica)**:
    ```bash
    # Si tu proyecto está en un repositorio Git
    # git clone <url-del-repositorio>
    # cd backapp_dev
    ```

2.  **Crear y Activar un Entorno Virtual**:
    Se recomienda encarecidamente utilizar un entorno virtual para aislar las dependencias del proyecto.
    ```bash
    python -m venv venv
    ```
    Para activar el entorno virtual:
    *   En Windows (PowerShell):
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```
    *   En macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Instalar Dependencias**:
    Asegúrate de tener el archivo `requirements.txt` actualizado con todas las librerías necesarias. Luego, ejecuta:
    ```bash
    pip install -r requirements.txt
    ```
    Si aún no tienes un `requirements.txt` o necesitas actualizarlo, puedes generarlo (después de instalar manualmente las librerías como `streamlit`, `python-dotenv`, `requests`) con:
    ```bash
    pip freeze > requirements.txt
    ```

4.  **Configurar Variables de Entorno**:
    Crea un archivo llamado `.env` en la raíz del proyecto (`c:\Users\Bernardo\Desktop\backapp_dev\.env`). Este archivo contendrá las credenciales y URLs necesarias.
    Un ejemplo del contenido del archivo `.env` podría ser:
    ```env
    API_KEY="TU_API_KEY_AQUI"
    WSDL_URL_CODIGOS="URL_DEL_SERVICIO_DE_CODIGOS"
    WSDL_URL_OPERACIONES="URL_DEL_SERVICIO_DE_OPERACIONES"
    WSDL_URL_SYNC="URL_DEL_SERVICIO_DE_SINCRONIZACION"
    WSDL_URL_AJUSTE="URL_DEL_SERVICIO_DE_DOCUMENTOS_DE_AJUSTE"
    WSDL_URL_FACTURACION="URL_DEL_SERVICIO_DE_FACTURACION_COMPRA_VENTA"
    ```
    **Nota**: Asegúrate de reemplazar los valores de ejemplo con tus credenciales y URLs reales. El archivo `.env` está incluido en el `.gitignore` para evitar que se suban credenciales sensibles al repositorio.

## Ejecutar la Aplicación

Una vez que el entorno esté configurado y las dependencias instaladas, puedes ejecutar la aplicación Streamlit con el siguiente comando desde la raíz del proyecto (`c:\Users\Bernardo\Desktop\backapp_dev`):

```bash
streamlit run app.py
```

Esto iniciará un servidor local y abrirá la aplicación en tu navegador web predeterminado.

## Estructura del Proyecto

```
backapp_dev/
├── .env                # Archivo de variables de entorno (no versionado)
├── .gitignore          # Especifica los archivos ignorados por Git
├── app.py              # Punto de entrada principal de la aplicación Streamlit
├── logger_config.py    # Configuración del sistema de logging
├── requirements.txt    # Lista de dependencias de Python
├── response_handler.py # Módulo para parsear respuestas del SIAT
├── pages/              # Directorio para las diferentes páginas de la app Streamlit
│   └── 1_Verificar_comunicacion.py # Página para verificar la comunicación
└── logs/               # Directorio para los archivos de log (creado automáticamente)
    ├── app_YYYYMMDD.log
    └── ... (otros archivos de log)
```

## Logging

La aplicación utiliza un sistema de logging configurado en `logger_config.py`. Los logs se guardan en el directorio `logs/` y se rotan diariamente. Diferentes módulos pueden tener sus propios archivos de log para una mejor organización.

---

Este `README.md` proporciona una buena base. Puedes expandirlo o modificarlo según evolucione tu proyecto.
