# Guía Técnica de Facturación Electrónica e Interoperabilidad

---

## 1. Facturación Electrónica

La **Facturación Electrónica** es una modalidad de emisión de Documentos Fiscales Digitales mediante el uso de tecnologías que garantizan su autenticidad, integridad y validez legal. Se fundamenta en el uso obligatorio de la **Firma Digital** y el intercambio de archivos en formato **XML**, conforme a los lineamientos técnicos establecidos por el **Servicio de Impuestos Nacionales (SIN)**.

### Características principales:

- Emisión de Facturas Digitales con **Firma Digital**.
- Impresión opcional de la Representación Gráfica de la Factura.
- Envío individual de Facturas firmadas digitalmente en **formato XML**.
- Envío agrupado por contingencia en paquetes XML firmados digitalmente.
- Envío masivo de Facturas mediante paquetes XML firmados digitalmente.

---

## 2. Esquema de Interoperabilidad

El siguiente flujo describe el proceso de interoperabilidad entre el Sistema Informático de Facturación (SIF) del emisor y los servicios del SIN:

### 2.1 Solicitud del CUFD

El SIF del emisor, previamente autorizado y con **CUIS vigente**, realiza la solicitud del **Código Único de Facturación Diaria (CUFD)** al SIN. Este código habilita la emisión de facturas por un período de 24 horas.

### 2.2 Validación y respuesta del SIN

El SIN valida la autenticidad del emisor y responde con los siguientes datos:

- CUFD.
- Código de Verificación.
- Dirección registrada de la sucursal o casa matriz.

### 2.3 Generación y firma de la Factura Digital

El SIF del contribuyente genera la Factura Digital en formato XML, firmada digitalmente utilizando certificados válidos. Posteriormente, se envía al SIN a través de los servicios web habilitados.

### 2.4 Validación por el SIN

El SIN procesa la solicitud y valida la estructura y cabecera de la factura. Las respuestas posibles son:

- **Validación correcta (proceso individual):** Se retorna el **Código de Recepción**.
- **Validación correcta (paquete de contingencia o masivo):** Se retorna un **Código de Recepción** para el paquete.
- **Errores de validación:** Se devuelve una lista de **códigos de error y mensajes**, que deben ser corregidos para el reenvío del archivo XML.

### 2.5 Envío al cliente final

El emisor puede enviar al cliente:
- El archivo XML firmado digitalmente.
- La Representación Gráfica de la Factura, como respaldo opcional en formato físico o digital.

### 2.6 Validación de paquetes (contingencia o masiva)

Cuando la emisión se realiza por paquetes, el SIN valida cada factura del conjunto individualmente. Los resultados posibles son:

- **Validación exitosa:** Se registran y consolidan todas las facturas del paquete.
- **Errores parciales:** Se aceptan facturas válidas y se rechazan las que presentan errores.  
  - Si el error es por NIT inválido o no verificado, el emisor puede utilizar un **Código de Excepción** para evitar el rechazo.

### 2.7 Resultado final de validación

El SIN remite el resultado final de la validación. En caso de observaciones, el emisor deberá corregir los errores y reenviar únicamente las facturas observadas.

---

## 3. Glosario Técnico – Códigos de Autorización

### CUIS – Código Único de Inicio de Sistemas
Identifica la relación entre el SIF, el contribuyente, la sucursal y el punto de venta. Tiene una vigencia de 365 días. Su obtención requiere el uso de un Token.

### CUFD – Código Único de Facturación Diaria
Permite la emisión de Documentos Fiscales Electrónicos durante un período de 24 horas. Se obtiene mediante la validación del contribuyente a través de un Token.

### CUF – Código Único de Factura
Generado automáticamente por el SIF en el momento de la emisión. Permite identificar de forma única cada Factura Digital.

### CAED – Código de Autorización para Emisión de Documentos
Asignado por el SIN para la emisión de Documentos Fiscales en las modalidades manual y prevalorada preimpresa.

### CAFC – Código Autorización Facturas Contingencia
Emitido por el SIN para autorizar la impresión y posterior emisión de facturas de contingencia.

### Número de Autorización
Generado automáticamente para la modalidad de Facturación Computarizada SFV.

> **Nota:** En los registros obligatorios ante el SIN, excepto en los aplicativos SIAT o “Mis Facturas”, donde se solicite el Número de Autorización, deberá consignarse el valor **99** cuando se utilicen Códigos de Autorización en modalidades como Facturación Electrónica en Línea, Computarizada en Línea, Portal Web en Línea o Manual.

---

## 4. Sucursales y Puntos de Venta

### Sucursales

Las sucursales son establecimientos secundarios donde se desarrolla alguna actividad económica del Contribuyente. Cada sucursal tiene una **dirección física** registrada en el **Padrón Nacional de Contribuyentes**.  
En el Sistema de Facturación, las facturas se emiten por sucursal o por la casa matriz (denominada **Sucursal 0**).

### Puntos de Venta

Un punto de venta es un lugar, dispositivo o medio asociado a una sucursal o casa matriz, desde donde se efectúa la venta de bienes o prestación de servicios. Puede ser:

- Fijo (ej. ventanilla de feria),
- Móvil (ej. camiones de reparto).

Aunque **no están registrados en el Padrón Nacional de Contribuyentes**, deben ser **registrados en el Sistema de Facturación** para poder emitir documentos fiscales. Tipos de puntos de venta:

- Comisionistas conforme normativa vigente.
- Ventanillas de Cobranza autorizadas por ASFI.
- Puntos Móviles de venta de bienes o servicios.
- Puntos de Venta de YPFB para venta de combustibles a precio internacional.
- Cajeros o dispositivos para emisión automática de facturas.
- Puntos de Venta Conjunta (habilitados para emisión conjunta).

### Consideraciones para uso de puntos de venta móviles

- Para contribuyentes bajo la **modalidad de Facturación Electrónica en Línea**, los puntos de venta móviles deben **tener capacidad de firmar digitalmente** las facturas o estar conectados a un servicio centralizado de firma.

- Según normativa vigente, los puntos de venta deben registrarse previamente a través de los **Servicios Web del SIN** o desde el **Portal Web**.

- Empresas que operan en **zonas sin acceso a internet**, podrán solicitar el uso excepcional mediante declaración jurada con justificación, a través del Portal Web del SIN.

---
