# Producto Mínimo Viable (MVP) - Sistema de Facturación Electrónica SIAT

## 1. Introducción y Objetivos del MVP

Este documento define las características y funcionalidades mínimas viables (MVP) para la primera versión del Sistema de Facturación Electrónica, diseñado para interactuar con los servicios web del Servicio de Impuestos Nacionales (SIAT) de Bolivia.

**Objetivos Principales del MVP:**

*   Permitir la emisión de facturas electrónicas en diferentes modalidades operativas exigidas por el SIAT (en línea, fuera de línea, masiva y por contingencia manual).
*   Asegurar la correcta formación, firma (cuando aplique), empaquetado y envío de los documentos fiscales a la Administración Tributaria.
*   Gestionar los códigos de autorización (CUIS, CUFD) necesarios para la operación.
*   Proporcionar un mecanismo básico para la verificación de la comunicación con los servicios del SIAT.
*   Cumplir con los requisitos técnicos y de formato establecidos por el SIAT para la facturación electrónica.

Este MVP se enfoca en las funcionalidades esenciales para que el sistema sea operativo y pueda ser utilizado para la facturación real, sentando las bases para futuras mejoras y expansiones.

## 2. Emisión y envío de Paquetes por Fuera de Linea

Se recurre a la emisión de Facturas fuera de línea (OFFLINE), cuando sucede algún evento significativos que impida la emisión de documentos fiscales en línea. En este caso las facturas se emiten individualmente y se agrupan en paquetes de hasta 500 documentos fiscales, para que luego de superada la contingencia se envíen los mismos a la Administración Tributaria a través de los servicios web correspondientes. El procedimiento a seguir es el siguiente:

*Primera Etapa* (Mientras dure la contingencia, proceder a emitir las facturas de manera individual)

    * Registar internamente el inicio del evento, junto con el motivo, para posteriormente
    * Generar Archivo XML asociado al Documento Fiscal, de acuerdo a su actividad económica (utilizar modalidad fuera de linea).
    * Firmar el archivo obtenido conforme estándar XMLDSig (sólo en el caso de la Modalidad Electrónica en Línea).
    * Validar contra el XSD asociado a objeto de comprobar que el XML está bien formado y se ajusta a una estructura definida.
    * Almacenar temporalmente de manera individual las Facturas generadas.

 *Segunda Etapa (una vez superada la contingencia)*

    * Recuperar las Facturas almacenadas en formato XML durante la etapa anterior.
    * Formar paquetes de hasta 500 Facturas.
    * Comprimir con Gzip, el archivo resultante debe ser enviado utilizando para ello la etiqueta archivo.
    * Obtener el HASH (SHA256) del archivo compreso obtenido en el paso anterior, mismo que debe ser enviado en la etiqueta hashArchivo.
    * Envío de Paquetes de Facturas:*
      * Consumir el servicio correspondiente para obtener un nuevo CUFD.
      * Registrar el evento significativo a través del servicio web correspondiente, indicando la fecha de inicio y fin del evento, así como el CUFD que fue usado para la emisión de facturas de contingencia.
      * Enviar los paquetes consumiendo el servicio "Recepción de Paquetes de facturas electrónicas o computarizadas". Si la transacción es exitosa, se devolverá el estado 901 (pendiente), el código de recepción del mismo y la transacción en True.
      * Validar la recepción consumiendo el servicio de "Validación de Paquetes de facturas electrónicas o computarizadas", mismo que devolverá el código de estado que puede ser 901 (pendiente), 904 (observada) o 908 (validado). En el caso de que existan observaciones se incluirá una lista de mensajes con códigos, descripciones, número de archivo y número de detalle de los errores y/o advertencias detectados en cada una de las facturas.

*Nota:* Como buena practica, debe mantenerse un registro de facturas sin código de respuesta, una vez superada la contingencia las mismas se verifiquen consumiendo el servicio verificaciónEstadoFactura a objeto de identificar si tienen registro o no en el Servicio de Impuestos Nacionales y proceder a su anulación en caso de ser necesario.

# Emisión y envío de Paquetes Masivos

Se utiliza el envío masivo cuando, por el giro de negocio de la empresa, se requiere la generación de Facturas en grandes cantidades por lotes, como es el caso de las entidades financieras, empresas de telecomunicaciones y de servicios básicos. Este modo de operación permite optimizar el envío de un alto volumen de documentos fiscales. Para poder utilizar la emisión de esta forma se debe registrar a través del Portal Web de la Administración Tributaria:

    * Periodicidad con la que se enviará: diario, semanal o mensual.
    * Tamaño de los paquetes: máximo 1000 Facturas.

*Primera Etapa*

    * Generar Archivo XML asociado al Documento Fiscal, de acuerdo a su actividad económica (utilizar modalidad en linea).
    * Firmar el archivo obtenido conforme estándar XMLDSig (sólo en el caso de la Modalidad Electrónica en Línea).
    * Validar contra el XSD asociado a objeto de comprobar que el XML está bien formado y se ajusta a una estructura definida.
    * Almacenar temporalmente de manera individual las Facturas generadas.

*Segunda Etapa*

    * Recuperar las Facturas almacenadas en formato XML durante la etapa anterior.
    * Formar paquetes de hasta 1000 Facturas.
    * Comprimir con Gzip el archivo resultante debe ser enviado en la etiqueta archivo.
    * Obtener el HASH (SHA256) del archivo compreso obtenido en el paso anterior, mismo que debe ser enviado en la etiqueta hashArchivo.
    * Envío de Paquetes de Facturas:
      * Consumir el servicio correspondiente para obtener un nuevo CUFD.
      * Enviar los paquetes consumiendo el servicio "Recepción de Paquetes de facturas electrónicas o computarizadas". Si la transacción es exitosa, se devolverá el estado 901 (pendiente), el código de recepción del mismo y la transacción en True.
      * Validar la recepción consumiendo el servicio de "Validación de Paquetes de facturas electrónicas o computarizadas", mismo que devolverá el código de estado que puede ser 901 (pendiente), 904 (observada) o 908 (validado). En el caso de que existan observaciones se incluirá una lista de mensajes con códigos, descripciones, número de archivo y número de detalle de los errores y/o advertencias detectados en cada una de las facturas. 

## 3. Emisión y envío de Paquetes por Contingencia

La emisión de Facturas Manuales de Contingencia se produce cuando el sistema que genera las facturas no esta disponible debido a un evento significativo de tipo (corte de energía, falla de software o falla de hardware). En este caso y para no parar el negocio, se puede recurrir a la emisión de Facturas Manuales de Contingencia (previamente solicitadas e impresas a través de una imprenta autorizada).  Superada el evento de contingencia se puede proceder de la siguiente manera:

**0. Envío del evento:**

    * Se debe registrar el evento a través del servicio disponible para el efecto indicando:

      * fecha de inicio (hasta el minuto mínimamente)
      * fecha de fin (hasta el minuto mínimamente)
      * código de evento (5,6 o 7)
      * cufd del evento (debe corresponder a la fecha en la cual se tuvo el evento)
      * cufd del envío 
      * descripción (descripción del evento ocurrido)

**1. Primera Etapa (Transcripción):**

    * Generar Archivo XML transcribiendo la información contenida en la factura manual, con tipo de emisión "fuera de linea" (2), utilizar el CUFD que estaba vigente al ingresar en contingencia y registrado en el evento (completar todos los campos requeridos)
    * Firmar el archivo obtenido conforme estándar XMLDSig (sólo en el caso de la Modalidad Electrónica en Línea).
    * Validar contra el XSD asociado a objeto de comprobar que el XML está bien formado y se ajusta a una estructura definida.
    * Almacenar temporalmente de manera individual las Facturas generadas.

**2. Segunda Etapa (Armado de paquetes):**

    * Recuperar las Facturas transcritas y en formato XML durante la etapa anterior.
    * Formar paquetes de hasta 500 Facturas.
    * Comprimir con Gzip, el archivo resultante debe ser enviado en la etiqueta archivo.
    * Obtener el HASH (SHA256) del archivo compreso obtenido en el paso anterior, mismo que debe ser enviado en la etiqueta hashArchivo.
    * Envío de Paquetes de Facturas:
      * Consumir el servicio correspondiente para obtener un nuevo CUFD .
      * Enviar los paquetes consumiendo el servicio "Recepción de Paquetes de facturas electrónicas o computarizadas", incluyendo el código de recepción del evento y el CAFC de las facturas transcritas. Si la transacción es exitosa, se devolverá el estado 901 (pendiente), el código de recepción del mismo y la transacción en True.
      * Validar la recepción consumiendo el servicio de "Validación de Paquetes de facturas electrónicas o computarizadas", mismo que devolverá el código de estado que puede ser 901 (pendiente), 904 (observada) o 908 (validado). En el caso de que existan observaciones se incluirá una lista de mensajes con códigos, descripciones, número de archivo y número de detalle de los errores y/o advertencias detectados en cada una de las facturas.

**Nota.**

    * Para el ambiente de pruebas (PILOTO) deberá solicitar CAFC para los documentos que esta autorizando, así como para las sucursales que probaran.
    * Los Códigos Especiales 99001 (Utilizado para consulados, embajadas, etc), el 99002 (Control Tributario) y el 99003 (Ventas Menores del Día) se deben enviar con el tipo de documento NIT y el código de Excepción en 1.
    * Si durante la emisión  se utiliza como tipo de documento C.I. o NIT el sistema emisor debe validar que el valor que se envia sea numérico.
    * El código de excepción debe enviarse por defecto con un valor de 0 (cero). Se envía con un valor de 1 (uno) solo si el Tipo de documento es un NIT pidiendo de esta manera al SIN no validar el mismo. Por otro lado, si la emisión es en fuera de linea y el tipo de documento NIT siempre enviar el código de excepción  con un valor de 1.
    * El tipo de emisión "CONTINGENCIA" que se obtiene al realizar la sincronización de catalogos es para uso exclusivo del SIN.

# CODIGOS DE AUTORIZACION #

Los Códigos de Autorización otorgados por el SIN o generados por el Sistema Informático de Facturación autorizan la emisión de Documentos Fiscales en función a parámetros establecidos. De acuerdo a su característica podrán o no ser consignados en los documentos fiscales autorizados por la Administración Tributaria. Estos son los Códigos de Autorización definidos para la Modalidad de Facturación Electrónica:

**CUIS (Código Único de Inicio de Sistemas)**. Dato alfanumérico generado por la Administración Tributaria que identifica la relación entre el Sistema de Facturación, credenciales, contribuyente, sucursal y opcionalmente al punto de venta. Tiene una vigencia de 365 días calendario. Para su obtención se utiliza un Token que valida la autenticidad del contribuyente.
**CUFD (Código Único de Facturación Diaria).** Dato alfanumérico generado por la Administración Tributaria con la información del Sistema de Facturación, que permite al Sujeto Pasivo o Tercero Responsable la emisión de Documentos Fiscales Electrónicos durante 24 horas. Para su obtención se utiliza Token que la autenticidad del contribuyente.
**CUF (Código Único de Factura).** Generado de forma automática al momento de la emisión de la Factura por el Sistema Informático de Facturación que permite la individualización de cada factura.
**CAFC (Código Autorización Facturas Contingencia).** Generado por la Administración Tributaria para la impresión y posterior emisión de facturas de contingencia. Se lo obtiene al efectuar la solicitud de impresión de facturas manuales de contingencia.

**Nota.** En el caso del uso de Facturas Prevaloradas en Línea, el sistema informático de facturación deberá solicitar la autorización de emisión para este tipo de documento, considerando el periodo, los rangos de emisión y precios fijos para dichos documentos. Esta solicitud devolverá un código de autorización que deberá ser incluido en la solicitud de emisión.
En los registros obligatorios a enviar a la Administración Tributaria, excepto en el Registro de Compras y Ventas o aplicativos SIAT o Mis facturas, donde se solicite el Numero de Autorización, deberá registrarse el valor noventa y nueve (99) cuando las citadas facturas consignen Códigos de Autorización emitidos en la Modalidad de Facturación Electrónica en Línea.

# CONTINGENCIA Y EVENTOS SIGNIFICATIVOS #

Los eventos significativos son hechos inherentes al Sistema informático de Facturación que intervienen en su funcionamiento o que podrían afectar la emisión de las Facturas Digitales. Deben ser registrados hasta 48 horas posteriores de finalizada la contingencia, a través del sistema autorizado por la Administración Tributaria y enviados automáticamente a través del servicio Web correspondiente.

Tipos de Eventos Significativos que generan contingencia

+----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **EVENTO SIGNIFICATIVO **                                            |                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                      | **DETALLE DE ACCIÓN**                                                                                                                                                                                                                                                                                                                                                                |
+----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                                   |
| *1) Corte del servicio de Internet*                                  |                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------------+                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                      | Emitir Documentos Fiscales digitales fuera de línea, conforme lo establecido en el Anexo Técnico de la presente Resolución.                                                                                                                                                                                                                                                       |
| *2) Inaccesibilidad al Servicio Web de la Administración Tributaria.*|                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------------+                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                                   |
|*3) Ingreso a zonas sin Internet por despliegue de puntos de venta.*  |                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------------+                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                                   |
| *4) Venta en Lugares sin internet.*                                  |                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                                   |
| *5) Virus informático o falla de software.*                          | Emitir  Facturas por Contingencia autorizadas por la Administración Tributaria, solicitadas con anterioridad por el Sujeto Pasivo del IVA o emitir  Documentos Fiscales Digitales usando de manera transitoria y por  contingencia la Modalidad de Facturación Portal Web en línea conforme  los aspectos técnicos establecidos en el Anexo Técnico de la presente  Resolución.  |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------------+                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                                   |
| *6) Cambio de infraestructura de sistema o falla de hardware.*       |                                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                      | Emitir  Facturas por Contingencia autorizadas por la Administración Tributaria,  solicitadas con anterioridad por el Sujeto Pasivo del IVA.                                                                                                                                                                                                                                       |
| *7) Corte de suministro de energía eléctrica.*                       |                                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

De producirse una contingencia, pero el sistema informático continua operativo, este deberá cambiar a la emisión de facturas fuera de línea, las facturas se emiten con el CUFD vigente hasta antes del corte. Las facturas emitidas se almacenan en paquetes que posteriormente serán enviados a la administración Tributaria, cuando la contingencia se haya superado. (Obtener un nuevo CUFD antes de registrar el evento significativo y enviar los paquetes, a fin de evitar posibles inconvenientes relacionados al tiempo de vigencia del CUFD durante el envío de los mismos de no hacerlo).

En caso de que no pueda utilizarse el sistema informático por falla de hardware, software o por corte de energía eléctrica, se deberán emitir facturas manuales de contingencia previamente aprovisionadas, superada la contingencia estas deberán ser transcritas utilizando para ello el CUFD que estaba vigente al ingresar en contingencia y enviadas a la Administración Tributaria a través del mismo sistema informático de facturación. (Obtener un nuevo CUFD antes de registrar el evento significativo y enviar los paquetes, a fin de evitar posibles inconvenientes relacionados al tiempo de vigencia del CUFD durante el envío de los mismos de no hacerlo).

Nota: Como buena practica, debe mantenerse un registro de facturas sin código de respuesta, a objeto de que una vez superada la contingencia se verifiquen las mismas consumiendo el servicio verificaciónEstadoFactura a objeto de identificar si fueron registradas o no en el Servicio de Impuestos Nacionales y de ser asi proceder a su anulación de ser necesario evitando duplicidades.

SI el tipo de documento utilizado en la emisión de una factura en fuera de linea es el NIT, se debe enviar el código de excepción con valor uno.