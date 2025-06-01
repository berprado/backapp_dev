# Solicitud del Código Único de Inicio de Sistemas (CUIS)

## Descripción General

De acuerdo con la normativa vigente, el **Código Único de Inicio de Sistemas (CUIS)** debe ser solicitado por cada **sucursal** y, si corresponde, por cada **punto de venta**. Esta solicitud se realiza a través del **Sistema Informático de Facturación (SIF)** autorizado, utilizando el **servicio web** expuesto por el Servicio de Impuestos Nacionales (SIN).

El CUIS es obligatorio para habilitar el funcionamiento de un sistema de facturación, y su obtención es el primer paso para emitir Documentos Fiscales Electrónicos.

---

## Método: `cuis`

El servicio implementa un método llamado `cuis`, al cual se debe enviar un objeto de tipo `SolicitudCuis`. A continuación se detalla la estructura de entrada y salida del método:

### **Entrada: Objeto `SolicitudCuis`**

| Campo              | Tipo de Dato     | Obligatorio | Descripción |
|--------------------|------------------|-------------|-------------|
| `codigoAmbiente`   | Numérico         | Sí          | Tipo de ambiente:<br>- Producción: `1`<br>- Pruebas/Piloto: `2` |
| `codigoSistema`    | Alfanumérico     | Sí          | Código asignado al SIF al momento de la autorización. |
| `nit`              | Numérico         | Sí          | Número de Identificación Tributaria del emisor. |
| `codigoModalidad`  | Numérico         | Sí          | Modalidad de facturación:<br>- Electrónica en Línea: `1`<br>- Computarizada en Línea: `2` |
| `codigoSucursal`   | Numérico         | Sí          | Identificador de la sucursal:<br>- Casa Matriz: `0`<br>- Sucursal: `1, 2, ...` |
| `codigoPuntoVenta` | Numérico         | No          | Código del punto de venta. En caso de no usar, enviar `0`. |

---

### **Salida**

| Campo              | Tipo de Dato     | Descripción |
|--------------------|------------------|-------------|
| `codigoCUIS`       | Alfanumérico     | CUIS generado para el sistema, sucursal y punto de venta especificado. |
| `fechaVigencia`    | Fecha UTC extendida | Fecha de vigencia del CUIS generado. |
| `transaccion`      | Boolean          | Indica si la operación fue procesada correctamente. |
| `CodigosRespuestas`| DTO[CodigosRespuesta] | Contiene el detalle de códigos y mensajes asociados a la operación. |

---

## Consideraciones Técnicas

- Este servicio **requiere el uso del Token Delegado** para autenticar la solicitud.
- El **CUIS tiene una vigencia de 365 días** calendario desde su emisión.
- Puede ser **renovado a partir del quinto día anterior a su vencimiento**.
- El sistema mostrará una **alerta automática** al obtener el CUFD si el CUIS está próximo a vencer.
- Al renovar el CUIS, **es obligatorio solicitar un nuevo CUFD** para continuar con la emisión de facturas electrónicas.

---

## Buenas prácticas

- Automatiza la verificación de vencimiento del CUIS como parte del proceso de obtención del CUFD.
- Valida previamente la existencia y vigencia del CUIS en cada emisión para evitar errores de autorización.
- Registra los CUIS obtenidos por sucursal y punto de venta de forma segura en el sistema para su reuso hasta su expiración.

---

## Ejemplo de flujo

1. El sistema verifica si existe un CUIS válido para la sucursal/punto de venta.
2. Si no existe o está por vencer (dentro de los 5 días antes), se invoca el servicio `cuis`.
3. Con el CUIS obtenido, se procede a solicitar el CUFD correspondiente para iniciar la facturación.

---
