# Solicitud de Código Único de Facturación Diaria (CUFD) - Masivo

## Descripción General

El **Código Único de Facturación Diaria (CUFD)** permite la emisión de Facturas Digitales durante un periodo de 24 horas.  
Según normativa vigente, cada combinación de **sucursal y punto de venta** debe contar con un CUFD vigente para poder emitir documentos fiscales válidos.

El método `solicitudCufdMasivo` permite a los **Sujetos Pasivos o Terceros Responsables** obtener múltiples CUFD en una única solicitud, optimizando así la operación del **Sistema Informático de Facturación (SIF)** autorizado.

---

## Método: `solicitudCufdMasivo`

Este método está diseñado para obtener múltiples CUFD asociados a distintas combinaciones de sucursales y puntos de venta en una sola transacción.

### **Entrada: Objeto `solicitudCufdMasivo`**

| Campo               | Tipo de Dato     | Obligatorio | Descripción |
|---------------------|------------------|-------------|-------------|
| `codigoAmbiente`    | Numérico         | Sí          | Tipo de ambiente:<br>- Producción: `1`<br>- Pruebas/Piloto: `2` |
| `codigoModalidad`   | Numérico         | Sí          | Modalidad de facturación:<br>- Electrónica en Línea: `1`<br>- Computarizada en Línea: `2` |
| `codigoSistema`     | Alfanumérico     | Sí          | Código del sistema asignado al momento de la autorización. |
| `nit`               | Numérico         | Sí          | Número de Identificación Tributaria del emisor. |
| `datosSolicitud`    | Lista de objetos | Sí          | Lista que agrupa las combinaciones `codigoSucursal`, `codigoPuntoVenta` y `cuis`. |

#### Subestructura: `datosSolicitud`

| Campo               | Tipo de Dato     | Obligatorio | Descripción |
|---------------------|------------------|-------------|-------------|
| `codigoSucursal`    | Numérico         | Sí          | Identificador de la sucursal:<br>- Casa Matriz: `0`<br>- Sucursal: `1, 2, ...` |
| `codigoPuntoVenta`  | Numérico         | No          | Código del punto de venta. Si no aplica, enviar `0`. |
| `cuis`              | Alfanumérico     | Sí          | CUIS vigente correspondiente a la sucursal/punto de venta. |

---

### **Salida**

| Campo                | Tipo de Dato             | Descripción |
|----------------------|--------------------------|-------------|
| `ListaCodigoCufd`    | Lista[Alfanumérico]      | Lista de CUFD generados para cada combinación solicitada. |
| `fechaVigencia`      | Fecha UTC Extendida      | Fecha y hora de vencimiento de cada CUFD generado. |
| `transaccion`        | Boolean                  | Indica si la operación fue exitosa. |
| `CodigosRespuestas`  | DTO[CodigosRespuesta]    | Lista de códigos y mensajes de respuesta por cada solicitud procesada. |

---

## Consideraciones Técnicas

- Este servicio **requiere el uso del Token Delegado** para la autenticación.
- La **vigencia del CUFD es de 24 horas** desde su generación.
- El número máximo de combinaciones aceptadas por solicitud es **1,000**. Para solicitudes mayores, se debe dividir la operación.
- El sistema puede **retornar alertas** si el CUIS correspondiente está próximo a vencer, recomendando su renovación.

---

## Ventajas del uso masivo

- Reduce el número de llamadas individuales al servicio CUFD.
- Permite sincronizar previamente todos los puntos de emisión activos.
- Mejora la escalabilidad del sistema de facturación en entornos distribuidos.

---

## Buenas Prácticas

- Automatizar la solicitud masiva de CUFD una vez al día, en horarios definidos.
- Validar que el CUIS esté vigente antes de generar cada solicitud.
- Dividir las solicitudes si se gestionan más de 1,000 combinaciones.

---

## Flujo sugerido de operación

1. El sistema identifica todas las combinaciones sucursal/punto de venta que requieren CUFD.
2. Agrupa hasta 1,000 combinaciones en un objeto `solicitudCufdMasivo`.
3. Envía la solicitud al servicio web.
4. Registra los CUFD obtenidos con su fecha de vigencia.
5. Usa el CUFD correspondiente en la emisión de cada factura durante el día.

---
