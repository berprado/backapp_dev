# Notificación de Certificado Revocado

## Descripción General

De acuerdo con la normativa vigente, el **Sistema Informático de Facturación (SIF)** del Sujeto Pasivo debe informar de manera inmediata la **revocación o suspensión de un certificado de firma digital** utilizado en la emisión de Facturas Digitales.

La invocación del método `solicitudNotificaRevocado` inhabilita automáticamente el **CUIS** y **CUFD** vigentes asociados, bloqueando la emisión de facturas hasta que una nueva firma digital válida sea registrada y habilitada.

---

## Método: `solicitudNotificaRevocado`

Este método permite notificar al Servicio de Impuestos Nacionales (SIN) sobre la revocación de un certificado digital previamente habilitado para firmar facturas electrónicas.

### **Entrada: Objeto `notificaCertificadoRevocado`**

| Campo               | Tipo de Dato     | Obligatorio | Descripción |
|---------------------|------------------|-------------|-------------|
| `codigoAmbiente`    | Numérico         | Sí          | Tipo de ambiente:<br>- Producción: `1`<br>- Pruebas/Piloto: `2` |
| `codigoSistema`     | Alfanumérico     | Sí          | Código asignado al SIF al momento de su autorización. |
| `nit`               | Numérico         | Sí          | Número de Identificación Tributaria del emisor. |
| `cuis`              | Alfanumérico     | Sí          | CUIS vigente correspondiente a la sucursal y/o punto de venta. |
| `codigoSucursal`    | Numérico         | Sí          | Identificador de la sucursal:<br>- Casa Matriz: `0`<br>- Sucursal: `1, 2, ...` |
| `fechaRevocacion`   | Date             | Sí          | Fecha en la que fue revocado o suspendido el certificado digital. |
| `razonRevocacion`   | Alfanumérico     | Sí          | Motivo o causa de la revocación del certificado. |
| `certificado`       | Alfanumérico     | Sí          | Contenido del certificado digital que ha sido revocado. |

---

### **Salida**

| Campo               | Tipo de Dato          | Descripción |
|---------------------|-----------------------|-------------|
| `transaccion`       | Boolean               | Indica si la operación fue procesada correctamente. |
| `codigosRespuestas` | DTO[codigosRespuesta] | Detalle de códigos y mensajes relacionados al resultado del servicio. |

---

## Consideraciones Técnicas

- **Este servicio requiere el uso del Token Delegado** para autenticar la operación.
- La notificación **inhabilita de forma inmediata** el CUIS y CUFD activos relacionados con el certificado revocado.
- A partir de la notificación, **no se podrá emitir ninguna Factura Digital** hasta que se registre un nuevo certificado digital válido y habilitado.

---

## Buenas Prácticas

- Implementar monitoreo automático del estado de los certificados utilizados en producción.
- Realizar la notificación de manera inmediata ante la revocación voluntaria o técnica de un certificado.
- Validar que el nuevo certificado esté correctamente registrado y activo antes de intentar emitir nuevas facturas.

---

## Flujo sugerido

1. El sistema detecta o gestiona la revocación del certificado de firma digital.
2. Se genera el objeto `notificaCertificadoRevocado` con los datos requeridos.
3. Se invoca el método `solicitudNotificaRevocado` para reportar el evento al SIN.
4. El sistema suspende automáticamente toda emisión de facturas.
5. Una vez habilitado un nuevo certificado, se reactiva la facturación mediante la solicitud de un nuevo CUIS y CUFD.

---
