# Solicitud del Código Único de Facturación Diaria (CUFD)

## Descripción General

El **Código Único de Facturación Diaria (CUFD)** es un identificador generado diariamente por la Administración Tributaria que habilita al **Sistema Informático de Facturación (SIF)** autorizado para la **emisión de Facturas Digitales durante un periodo de 24 horas**.

De acuerdo con la normativa vigente, la solicitud del CUFD debe realizarse de forma **obligatoria y periódica** para cada sucursal y, si corresponde, punto de venta. La obtención se realiza mediante el **consumo del Servicio Web** proporcionado por el SIN.

---

## Método: `solicitudCufd`

Este método permite al contribuyente autorizado obtener un nuevo CUFD con base en su CUIS vigente y configuración operativa.

### **Entrada: Objeto `solicitudCufd`**

| Campo              | Tipo de Dato     | Obligatorio | Descripción |
|--------------------|------------------|-------------|-------------|
| `codigoAmbiente`   | Numérico         | Sí          | Tipo de ambiente:<br>- Producción: `1`<br>- Pruebas/Piloto: `2` |
| `codigoSistema`    | Alfanumérico     | Sí          | Código asignado al SIF al momento de su autorización. |
| `nit`              | Numérico         | Sí          | Número de Identificación Tributaria del emisor. |
| `codigoModalidad`  | Numérico         | Sí          | Modalidad de facturación:<br>- Electrónica en Línea: `1`<br>- Computarizada en Línea: `2` |
| `cuis`             | Alfanumérico     | Sí          | CUIS vigente correspondiente a la sucursal y/o punto de venta. |
| `codigoSucursal`   | Numérico         | Sí          | Identificador de la sucursal:<br>- Casa Matriz: `0`<br>- Sucursal: `1, 2, ...` |
| `codigoPuntoVenta` | Numérico         | No          | Código del punto de venta. En caso de no usar, enviar `0`. |

---

### **Salida**

| Campo              | Tipo de Dato         | Descripción |
|--------------------|----------------------|-------------|
| `codigoCUFD`       | Alfanumérico         | CUFD generado válido por 24 horas. |
| `fechaVigencia`    | Fecha UTC Extendida  | Fecha y hora de vencimiento del CUFD. |
| `codigoControl`    | Alfanumérico         | Código de control de seguridad generado junto con el CUFD. |
| `direccion`        | Alfanumérico         | Dirección asociada a la sucursal registrada en padrón tributario. |
| `transaccion`      | Boolean              | Indica si la operación fue exitosa. |
| `codigosRespuestas`| DTO[codigosRespuesta]| Contiene los códigos y mensajes devueltos por el servicio. |

---

## Consideraciones Técnicas

- Este servicio **requiere el uso del Token Delegado** para autenticación.
- El CUFD tiene una **vigencia exacta de 24 horas** desde su generación.
- La emisión de Facturas Digitales **solo es válida si se incluye un CUFD activo y vigente**.
- Si el CUIS está próximo a expirar, el sistema retornará una **alerta preventiva** al obtener el CUFD, recomendando renovar el CUIS antes de su vencimiento.
- Cada vez que se renueve el CUIS, se deberá **obtener un nuevo CUFD** para poder continuar con la emisión de facturas.

---

## Buenas Prácticas

- Programar la solicitud del CUFD automáticamente una vez al día, validando la vigencia del CUIS antes de iniciar el proceso.
- Validar siempre localmente la fecha de expiración del CUFD antes de emitir una factura.
- Sincronizar la solicitud del CUFD en horarios definidos (ej. al inicio de jornada o a medianoche) para evitar errores por vencimiento.

---

## Flujo de Operación Sugerido

1. Verificar si el CUIS es válido y vigente.
2. Invocar el método `solicitudCufd` con los datos correspondientes.
3. Almacenar el CUFD junto con su fecha de vigencia.
4. Utilizar este CUFD en cada factura generada dentro del período de 24 horas.
5. Repetir el proceso diariamente.

---
