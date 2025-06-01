Verifica Comunicación
Este servicio recibe la solicitud de verificación de comunicación, registra la misma y devuelve un código de comunicación exitosa

+-------------------------------------------------------------------------------------------------------------+
| Nombre Método: verificarComunicacion                                                                        |
+----------+------------+------------------+--------------+--------------------------------------+------------+
|          |            |                  |              |                                      |            |
| Entrada  | Tipo Dato  | Obligatorio      | Descripción  | Salida                               | Tipo Dato  |
+----------+------------++-----------------+--------------+--------------------------------------+------------+
|          |             |                 |              |                                      |            |
| ninguna  | ninguno     | No corresponde  | ninguna      | return = 926 (comunicación exitosa)  | Numérico   |
+----------+-------------+-----------------+--------------+--------------------------------------+------------+

#Solicitud verificar comunicacion codigos:

```
POST https://pilotosiatservicios.impuestos.gob.bo/v2/FacturacionCodigos HTTP/1.1
Accept-Encoding: gzip,deflate
Content-Type: text/xml;charset=UTF-8
SOAPAction: ""
apikey: TokenApi eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJCT0xJVklBTkZPT0QiLCJjb2RpZ29TaXN0ZW1hIjoiN0M4QUZCQzgzOEQ3NTMwNDFDMTRENjYiLCJuaXQiOiJINHNJQUFBQUFBQUFBRE0yTVRHd05ETXdNZ0VBREF1Nk9Ra0FBQUE9IiwiaWQiOjYzNTMzOCwiZXhwIjoxNzU2NjkwMDc5LCJpYXQiOjE3MjUxNjg0NTAsIm5pdERlbGVnYWRvIjozNDQwOTYwMjQsInN1YnNpc3RlbWEiOiJTRkUifQ.3wjT4C5kD4PdJ78RQ0MQrRyZQRw7JtZf3UFhUxsYm7Ts-PmzXOEjUMPJnUaCTHnhzRIuBRxzLRAyVbtbOlzaOw
Content-Length: 239
Host: pilotosiatservicios.impuestos.gob.bo
Connection: Keep-Alive
User-Agent: Apache-HttpClient/4.5.5 (Java/16.0.2)

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:siat="https://siat.impuestos.gob.bo/">
	<soapenv:Header/>
	<soapenv:Body>
		<siat:verificarComunicacion/>
	</soapenv:Body>
</soapenv:Envelope>
```

#Reespuesta verificacion comunicacion codigos:

```
HTTP/1.1 200 
Date: Sun, 08 Sep 2024 01:34:35 GMT
Content-Type: text/xml;charset=UTF-8
Content-Length: 397
Connection: keep-alive

<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
	<soap:Body>
		<ns2:verificarComunicacionResponse xmlns:ns2="https://siat.impuestos.gob.bo/">
			<RespuestaComunicacion>
				<mensajesList>
					<codigo>926</codigo>
					<descripcion>COMUNICACION EXITOSA</descripcion>
				</mensajesList>
				<transaccion>true</transaccion>
			</RespuestaComunicacion>
		</ns2:verificarComunicacionResponse>
	</soap:Body>
</soap:Envelope>
```

#Solicitar verificar comunicación operaciones:

```
POST https://pilotosiatservicios.impuestos.gob.bo/v2/FacturacionOperaciones HTTP/1.1
Accept-Encoding: gzip,deflate
Content-Type: text/xml;charset=UTF-8
SOAPAction: ""
apikey: TokenApi eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJCT0xJVklBTkZPT0QiLCJjb2RpZ29TaXN0ZW1hIjoiN0M4QUZCQzgzOEQ3NTMwNDFDMTRENjYiLCJuaXQiOiJINHNJQUFBQUFBQUFBRE0yTVRHd05ETXdNZ0VBREF1Nk9Ra0FBQUE9IiwiaWQiOjYzNTMzOCwiZXhwIjoxNzU2NjkwMDc5LCJpYXQiOjE3MjUxNjg0NTAsIm5pdERlbGVnYWRvIjozNDQwOTYwMjQsInN1YnNpc3RlbWEiOiJTRkUifQ.3wjT4C5kD4PdJ78RQ0MQrRyZQRw7JtZf3UFhUxsYm7Ts-PmzXOEjUMPJnUaCTHnhzRIuBRxzLRAyVbtbOlzaOw
Content-Length: 239
Host: pilotosiatservicios.impuestos.gob.bo
Connection: Keep-Alive
User-Agent: Apache-HttpClient/4.5.5 (Java/16.0.2)

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:siat="https://siat.impuestos.gob.bo/">
	<soapenv:Header/>
	<soapenv:Body>
		<siat:verificarComunicacion/>
	</soapenv:Body>
</soapenv:Envelope>
```

#Respuesta verificacion comunicacion operaciones:

``` 
HTTP/1.1 200 
Date: Sun, 08 Sep 2024 01:43:31 GMT
Content-Type: text/xml;charset=UTF-8
Content-Length: 367
Connection: keep-alive

<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
	<soap:Body>
		<ns2:verificarComunicacionResponse xmlns:ns2="https://siat.impuestos.gob.bo/">
			<return>
				<mensajesList>
					<codigo>926</codigo>
					<descripcion>COMUNICACION EXITOSA</descripcion>
				</mensajesList>
				<transaccion>true</transaccion>
			</return>
		</ns2:verificarComunicacionResponse>
	</soap:Body>
</soap:Envelope>
```

#Solicitud verificar comunicacion sincronizaciones:

```
POST https://pilotosiatservicios.impuestos.gob.bo/v2/FacturacionSincronizacion HTTP/1.1
Accept-Encoding: gzip,deflate
Content-Type: text/xml;charset=UTF-8
SOAPAction: ""
apikey: TokenApi eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJCT0xJVklBTkZPT0QiLCJjb2RpZ29TaXN0ZW1hIjoiN0M4QUZCQzgzOEQ3NTMwNDFDMTRENjYiLCJuaXQiOiJINHNJQUFBQUFBQUFBRE0yTVRHd05ETXdNZ0VBREF1Nk9Ra0FBQUE9IiwiaWQiOjYzNTMzOCwiZXhwIjoxNzU2NjkwMDc5LCJpYXQiOjE3MjUxNjg0NTAsIm5pdERlbGVnYWRvIjozNDQwOTYwMjQsInN1YnNpc3RlbWEiOiJTRkUifQ.3wjT4C5kD4PdJ78RQ0MQrRyZQRw7JtZf3UFhUxsYm7Ts-PmzXOEjUMPJnUaCTHnhzRIuBRxzLRAyVbtbOlzaOw
Content-Length: 239
Host: pilotosiatservicios.impuestos.gob.bo
Connection: Keep-Alive
User-Agent: Apache-HttpClient/4.5.5 (Java/16.0.2)

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:siat="https://siat.impuestos.gob.bo/">
	<soapenv:Header/>
	<soapenv:Body>
		<siat:verificarComunicacion/>
	</soapenv:Body>
</soapenv:Envelope>
```

#Respuesta verificacion comunicacion sincronizaciones:

```
HTTP/1.1 200 
Date: Sun, 08 Sep 2024 01:57:10 GMT
Content-Type: text/xml;charset=UTF-8
Content-Length: 367
Connection: keep-alive

<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
	<soap:Body>
		<ns2:verificarComunicacionResponse xmlns:ns2="https://siat.impuestos.gob.bo/">
			<return>
				<mensajesList>
					<codigo>926</codigo>
					<descripcion>COMUNICACION EXITOSA</descripcion>
				</mensajesList>
				<transaccion>true</transaccion>
			</return>
		</ns2:verificarComunicacionResponse>
	</soap:Body>
</soap:Envelope>
```


#Solicitud verificar comunicacion Documentos de Ajuste:

```
POST https://pilotosiatservicios.impuestos.gob.bo/v2/ServicioFacturacionDocumentoAjuste HTTP/1.1
Accept-Encoding: gzip,deflate
Content-Type: text/xml;charset=UTF-8
SOAPAction: ""
apikey: TokenApi eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJCT0xJVklBTkZPT0QiLCJjb2RpZ29TaXN0ZW1hIjoiN0M4QUZCQzgzOEQ3NTMwNDFDMTRENjYiLCJuaXQiOiJINHNJQUFBQUFBQUFBRE0yTVRHd05ETXdNZ0VBREF1Nk9Ra0FBQUE9IiwiaWQiOjYzNTMzOCwiZXhwIjoxNzU2NjkwMDc5LCJpYXQiOjE3MjUxNjg0NTAsIm5pdERlbGVnYWRvIjozNDQwOTYwMjQsInN1YnNpc3RlbWEiOiJTRkUifQ.3wjT4C5kD4PdJ78RQ0MQrRyZQRw7JtZf3UFhUxsYm7Ts-PmzXOEjUMPJnUaCTHnhzRIuBRxzLRAyVbtbOlzaOw
Content-Length: 239
Host: pilotosiatservicios.impuestos.gob.bo
Connection: Keep-Alive
User-Agent: Apache-HttpClient/4.5.5 (Java/16.0.2)

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:siat="https://siat.impuestos.gob.bo/">
	<soapenv:Header/>
	<soapenv:Body>
		<siat:verificarComunicacion/>
	</soapenv:Body>
</soapenv:Envelope>
```


#Respuesta verificar comunicacion Documentos de Ajuste:


```
HTTP/1.1 200 
Date: Sun, 08 Sep 2024 02:02:46 GMT
Content-Type: text/xml;charset=UTF-8
Content-Length: 271
Connection: keep-alive

<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
	<soap:Body>
		<ns2:verificarComunicacionResponse xmlns:ns2="https://siat.impuestos.gob.bo/">
			<return>
				<transaccion>true</transaccion>
			</return>
		</ns2:verificarComunicacionResponse>
	</soap:Body>
</soap:Envelope>
```

#Solicitud verificar comunicacion Facturacion:

```
POST https://pilotosiatservicios.impuestos.gob.bo/v2/ServicioFacturacionCompraVenta HTTP/1.1
Accept-Encoding: gzip,deflate
Content-Type: text/xml;charset=UTF-8
SOAPAction: ""
apikey: TokenApi eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJCT0xJVklBTkZPT0QiLCJjb2RpZ29TaXN0ZW1hIjoiN0M4QUZCQzgzOEQ3NTMwNDFDMTRENjYiLCJuaXQiOiJINHNJQUFBQUFBQUFBRE0yTVRHd05ETXdNZ0VBREF1Nk9Ra0FBQUE9IiwiaWQiOjYzNTMzOCwiZXhwIjoxNzU2NjkwMDc5LCJpYXQiOjE3MjUxNjg0NTAsIm5pdERlbGVnYWRvIjozNDQwOTYwMjQsInN1YnNpc3RlbWEiOiJTRkUifQ.3wjT4C5kD4PdJ78RQ0MQrRyZQRw7JtZf3UFhUxsYm7Ts-PmzXOEjUMPJnUaCTHnhzRIuBRxzLRAyVbtbOlzaOw
Content-Length: 239
Host: pilotosiatservicios.impuestos.gob.bo
Connection: Keep-Alive
User-Agent: Apache-HttpClient/4.5.5 (Java/16.0.2)

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:siat="https://siat.impuestos.gob.bo/">
	<soapenv:Header/>
	<soapenv:Body>
		<siat:verificarComunicacion/>
	</soapenv:Body>
</soapenv:Envelope>
```

#Respuesta verificar comunicacion Facturacion:

```
HTTP/1.1 200 
Date: Sun, 08 Sep 2024 02:14:14 GMT
Content-Type: text/xml;charset=UTF-8
Content-Length: 271
Connection: keep-alive

<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
	<soap:Body>
		<ns2:verificarComunicacionResponse xmlns:ns2="https://siat.impuestos.gob.bo/">
			<return>
				<transaccion>true</transaccion>
			</return>
		</ns2:verificarComunicacionResponse>
	</soap:Body>
</soap:Envelope>
```