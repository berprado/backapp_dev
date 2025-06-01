# Verificación de NIT

## Descripción General

El servicio **verificarNit** permite validar si un **Número de Identificación Tributaria (NIT)** está registrado y es válido ante el Servicio de Impuestos Nacionales (SIN).  
Este proceso forma parte del cumplimiento normativo para la emisión de Facturas Digitales a través de un **Sistema Informático de Facturación (SIF)** autorizado.

### Recomendaciones de uso:

- Para **clientes frecuentes o registrados**, se recomienda realizar la verificación de manera anticipada y almacenar el resultado.
- Para **clientes eventuales o no registrados**, se debe realizar la verificación al momento de emitir la factura.

---

## Método: `verificarNit`

El método `verificarNit` recibe un objeto de tipo `SolicitudVerificarNit` y devuelve el resultado de la validación del NIT.

### **Entrada: Objeto `SolicitudVerificarNit`**

| Campo                | Tipo de Dato     | Obligatorio | Descripción |
|----------------------|------------------|-------------|-------------|
| `codigoAmbiente`     | Numérico         | Sí          | Tipo de ambiente:<br>- Producción: `1`<br>- Pruebas/Piloto: `2` |
| `codigoSistema`      | Alfanumérico     | Sí          | Código del sistema asignado al momento de la autorización. |
| `nit`                | Numérico         | Sí          | NIT del emisor de la factura. |
| `codigoModalidad`    | Numérico         | Sí          | Modalidad de facturación:<br>- Electrónica en Línea: `1`<br>- Computarizada en Línea: `2` |
| `codigoSucursal`     | Numérico         | Sí          | Código de la sucursal:<br>- Casa Matriz: `0`<br>- Sucursal: `1, 2, ...` |
| `nitParaVerificacion`| Numérico         | Sí          | NIT del cliente a verificar. |

---

### **Salida**

| Campo         | Tipo de Dato     | Descripción |
|---------------|------------------|-------------|
| `transaccion` | Boolean          | Indica si la verificación fue procesada correctamente. |
| `mensajes`    | Lista            | Lista de mensajes con códigos y descripciones del resultado (ej. válido, inexistente, inactivo, etc.). |

---

## Consideraciones Técnicas

- El servicio **requiere el uso del Token Delegado**.
- La verificación previa evita rechazos por NIT inválidos durante la validación de la Factura Digital.
- La verificación de NIT no genera CUFD ni está vinculada directamente con el proceso de emisión, pero **es obligatoria como control previo**.

---

## Buenas Prácticas

- Implementar un proceso automático de verificación al registrar o actualizar los datos de clientes frecuentes.
- En caso de NIT inválido o no verificado, el sistema debe manejar el caso según normativa: permitir la emisión con un **Código de Excepción** o impedirla.
- Registrar localmente los resultados de las verificaciones para trazabilidad y auditoría.

---

## Flujo sugerido de uso

1. El sistema captura el NIT del cliente previo a la emisión.
2. Invoca el método `verificarNit` con el NIT objetivo.
3. Si el resultado es válido, continúa con la emisión.
4. Si el resultado es negativo, se muestra advertencia al usuario o se aplica la lógica del Código de Excepción (si está habilitada).
5. Se registra el resultado de la verificación.

---
