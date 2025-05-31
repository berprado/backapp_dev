---

## Facturación Electrónica

La facturación electrónica es un método para emitir facturas digitales firmadas electrónicamente. 
Este proceso incluye el uso de un Token (propio o delegado) a través de un Sistema Informático de Facturación autorizado por la Administración Tributaria. 
Las facturas son enviadas, registradas y validadas en los servidores de la base de datos del SIN (Servicio de Impuestos Nacionales).

### Características:

- Uso de la Firma Digital.
- Impresión opcional de la Factura Digital.
- Envío individual de la Factura firmada digitalmente en formato XML.
- Envío agrupado de Facturas en formato XML firmadas digitalmente por contingencia.
- Envío masivo de Facturas en formato XML firmadas digitalmente en forma de paquetes.

---

## Esquema de Interoperabilidad

1. El Sistema Informático de Facturación del emisor solicita al SIN el Código Único de Facturación Diaria (CUFD), que habilita la emisión de facturas por un periodo de 24 horas.
2. El SIN verifica la información del emisor y devuelve los códigos de verificación y CUFD, junto con la dirección de la sucursal o casa matriz.
3. El Sistema Informático de Facturación del contribuyente utiliza el CUFD y los datos de emisión para generar el archivo XML (factura digital), que debe ser firmado digitalmente y enviado a través de los servicios correspondientes del SIN.
4. El SIN recibe la solicitud de recepción y procede a validar la cabecera, devolviendo la siguiente información:
   a) Si la validación es correcta en un proceso individual en línea, retorna el código de recepción.
   b) Si la validación es correcta en un proceso por paquete de contingencia o masivo, retorna el código de recepción.
   c) Si la validación presenta errores, retorna una lista de códigos y mensajes de error para que el emisor proceda a su corrección y posterior reenvío.
5. El Sistema envía por correo u otro medio la representación gráfica y el XML al cliente. Si el cliente desea tener un respaldo de la emisión de la Factura Digital, el emisor puede imprimir la representación gráfica.
6. Cuando la emisión de la Factura Digital es por paquete de contingencia o emisión masiva, el SIN valida la información contenida en el paquete de manera individual. Los resultados pueden ser:
   a) Registrar y consolidar la Factura Digital para la emisión por contingencia o masiva en caso de no existir errores.
   b) En caso de existir errores, se observa el paquete, se registran las facturas correctas y se rechazan las que contengan errores. Si el tipo de documento es NIT y el número de documento no es válido o no ha sido validado previamente, el emisor puede enviar el código de excepción para que la factura no sea rechazada.
7. El SIN retorna los resultados del proceso de validación descritos en el punto 6. En caso de existir observaciones, deberán ser subsanadas y posteriormente reenviar la Factura Digital.

---

---

## Factura Electrónica

Una Factura Electrónica es un documento digital de índole fiscal emitido a través de un Sistema Informático de Facturación autorizado por la Administración Tributaria. 
Su existencia es digital y debe ser registrada y validada en la base de datos del Servicio de Impuestos Nacionales (SIN).

### Requisitos para su emisión:

- **Token de acceso**: Puede ser propio o delegado (en el caso de un proveedor) y la Firma Digital del Sujeto Pasivo en la Modalidad de Facturación Electrónica en Línea.
- **Token de acceso delegado**: (en el caso de un sistema proveedor) o propio, y la huella del archivo XML en la Modalidad de Facturación Computarizada en Línea.
- **Credenciales de acceso**: Otorgadas por la Administración Tributaria en la Modalidad de Facturación Portal Web en Línea.

### XML

Las facturas electrónicas se envían al SIN utilizando XML, que es un tipo de lenguaje de marcado o conjunto de códigos (denominados etiquetas) que definen la estructura y el significado de los datos. 
A continuación, se describe de manera general la estructura de una factura computarizada:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<facturaComputarizadaCompraVenta xsi:noNamespaceSchemaLocation="facturaComputarizadaCompraVenta.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<cabecera>
		<nitEmisor>1003579028</nitEmisor>
		<razonSocialEmisor>Carlos Loza</razonSocialEmisor>
		<municipio>La Paz</municipio>
		<telefono>78595684</telefono>
		<numeroFactura>1</numeroFactura>
		<cuf>44AAEC00DBD34C53C3E2CCE1A3FA7AF1E2A08606A667A75AC82F24C74</cuf>
		<cufd>BQUE+QytqQUDBKVUFOSVRPQkxVRFZNVFVJBMDAwMDAwM</cufd>
		<codigoSucursal>0</codigoSucursal>
		<direccion>AV. JORGE LOPEZ #123</direccion>
		<codigoPuntoVenta xsi:nil="true"/>
		<fechaEmision>2021-10-06T16:03:48.675</fechaEmision>
		<nombreRazonSocial>Mi razon social</nombreRazonSocial>
		<codigoTipoDocumentoIdentidad>1</codigoTipoDocumentoIdentidad>
		<numeroDocumento>5115889</numeroDocumento>
		<complemento xsi:nil="true"/>
		<codigoCliente>51158891</codigoCliente>
		<codigoMetodoPago>1</codigoMetodoPago>
		<numeroTarjeta xsi:nil="true"/>
		<montoTotal>99</montoTotal>
		<montoTotalSujetoIva>99</montoTotalSujetoIva>
		<codigoMoneda>1</codigoMoneda>
		<tipoCambio>1</tipoCambio>
		<montoTotalMoneda>99</montoTotalMoneda>
		<montoGiftCard xsi:nil="true"/>
		<descuentoAdicional>1</descuentoAdicional>
		<codigoExcepcion xsi:nil="true"/>
		<cafc xsi:nil="true"/>
		<leyenda>Ley N° 453: Tienes derecho a recibir información sobre las características y contenidos de los servicios que utilices.</leyenda>
		<usuario>pperez</usuario>
		<codigoDocumentoSector>1</codigoDocumentoSector>
	</cabecera>
	<detalle>
		<actividadEconomica>451010</actividadEconomica>
		<codigoProductoSin>49111</codigoProductoSin>
		<codigoProducto>JN-131231</codigoProducto>
		<descripcion>MI PRODUCTO O SERVICIO</descripcion>
		<cantidad>1</cantidad>
		<unidadMedida>1</unidadMedida>
		<precioUnitario>100</precioUnitario>
		<montoDescuento>0</montoDescuento>
		<subTotal>100</subTotal>
		<numeroSerie>124548</numeroSerie>
		<numeroImei xsi:nil="true"/>
	</detalle>
</facturaComputarizadaCompraVenta>
```

### Servicios SOAP

Las facturas electrónicas son enviadas a la Administración Tributaria utilizando servicios SOAP.
Los servicios SOAP, o simplemente conocidos como Web Services, basan su comunicación en el protocolo SOAP, que define cómo dos objetos en diferentes procesos pueden comunicarse intercambiando datos mediante XML.

---
