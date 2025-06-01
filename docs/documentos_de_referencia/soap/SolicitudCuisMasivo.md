# Solicitud de Código Único de Inicio de Sistemas (CUIS) - Masivo

## Descripción General

El **CUIS (Código Único de Inicio de Sistemas)** es generado por la Administración Tributaria y representa la relación única entre el **Sistema Informático de Facturación (SIF)**, las **credenciales**, el **contribuyente**, la **sucursal** y, opcionalmente, el **punto de venta**.

Este código es inalterable y debe ser incluido obligatoriamente en cada **Factura Digital**. Para facilitar la gestión masiva de puntos de emisión, se habilita este servicio que permite **obtener múltiples CUIS de manera simultánea**, evitando llamadas individuales por cada combinación sucursal/punto de venta.

---

## Método: `SolicitudCuisMasivo`

Este método recibe un objeto del tipo `SolicitudCuisMasivo`, el cual agrupa todas las solicitudes que se desean realizar en un solo envío.

### **Entrada: Objeto `SolicitudCuisMasivo`**

| Campo               | Tipo de Dato       | Obligatorio | Descripción |
|---------------------|--------------------|-------------|-------------|
| `codigoAmbiente`    | Numérico           | Sí          | Tipo de ambiente:<br>- Producción: `1`<br>- Pruebas/Piloto: `2` |
| `codigoModalidad`   | Numérico           | Sí          | Modalidad de facturación:<br>- Electrónica en Línea: `1`<br>- Computarizada en Línea: `2` |
| `codigoSistema`     | Alfanumérico       | Sí          | Código asignado al SIF al momento de su autorización. |
| `nit`               | Numérico           | Sí          | Número de Identificación Tributaria del contribuyente emisor. |
| `datosSolicitud`    | Lista de objetos   | Sí          | Agrupador de pares `codigoSucursal` y `codigoPuntoVenta`. Permite solicitar múltiples CUIS. |

#### Subestructura: `datosSolicitud`

| Campo               | Tipo de Dato | Obligatorio | Descripción |
|---------------------|--------------|-------------|-------------|
| `codigoSucursal`    | Numérico     | Sí          | Identificador de la sucursal:<br>- Casa Matriz: `0`<br>- Sucursal: `1, 2, ...` |
| `codigoPuntoVenta`  | Numérico     | No          | Código del punto de venta. Si no se utiliza, enviar `0`. |

---

### **Salida**

| Campo               | Tipo de Dato          | Descripción |
|---------------------|-----------------------|-------------|
| `listaCodigosCuis`  | Lista[Alfanumérico]   | Listado de CUIS generados por cada combinación sucursal/punto de venta. |
| `fechaVigencia`     | Fecha UTC extendida   | Fecha hasta la cual es válido cada CUIS retornado. |
| `transaccion`       | Boolean               | Indica si la operación fue procesada exitosamente. |
| `codigosRespuesta`  | DTO[codigosRespuesta] | Detalle de la respuesta por cada entrada enviada. |

---

## Consideraciones Técnicas

- Este servicio **requiere el uso del Token Delegado** para la autenticación de la solicitud.
- Cada CUIS tiene una **vigencia de 365 días calendario**.
- Puede ser **renovado a partir del quinto día antes de su vencimiento**.
- Al solicitar un nuevo CUIS, **se debe obtener también un nuevo CUFD** para que la emisión de facturas continúe de forma válida.
- El sistema emitirá **alertas automáticas** durante la solicitud de CUFD si el CUIS está próximo a expirar.

---

## Ventajas del uso masivo

- Optimiza la sincronización de puntos de venta distribuidos.
- Reduce el número de llamadas al servicio.
- Mejora la escalabilidad del sistema de facturación ante altas operaciones simultáneas.

---

## Buenas Prácticas

- Automatizar la renovación del CUIS en función de la fecha de vigencia.
- Validar localmente la existencia de un CUIS activo por combinación Sucursal/Punto de Venta antes de emitir una factura.
- Mantener un sistema de registro de CUIS por canal de emisión para trazabilidad.

---

## Ejemplo de flujo:

1. El sistema evalúa qué puntos de venta o sucursales no tienen un CUIS vigente.
2. Agrupa todas las combinaciones necesarias en un solo objeto `SolicitudCuisMasivo`.
3. Invoca el servicio y obtiene una lista de CUIS válidos.
4. Registra cada CUIS en el sistema, asociado a su sucursal/punto de venta.
5. Solicita los CUFD respectivos para iniciar el proceso de facturación.

---
