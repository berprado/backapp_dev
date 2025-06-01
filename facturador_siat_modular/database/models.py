# Definiciones de los modelos de datos (ej. Factura, Cliente, EventoContingencia)
# Ejemplo usando SQLAlchemy:

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Numeric, Text, func, UniqueConstraint # Float ya no es necesario si todos los flotantes se convierten a Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# La configuración de la base de datos y las importaciones necesarias para Alembic
# se manejan en alembic/env.py. Los modelos no necesitan importar 'config' directamente
# ni manipular sys.path aquí.

Base = declarative_base()

class Empresa(Base):
    __tablename__ = "empresas"
    id = Column(Integer, primary_key=True, index=True)
    nit = Column(String(20), unique=True, index=True, nullable=False)
    razon_social = Column(String(255), nullable=False)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

    sucursales = relationship("Sucursal", back_populates="empresa")

class Sucursal(Base):
    __tablename__ = "sucursales"
    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)
    codigo_sucursal_siat = Column(Integer, nullable=False) # Código 0 para Casa Matriz
    descripcion = Column(String(255))
    direccion = Column(String(500))
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

    empresa = relationship("Empresa", back_populates="sucursales")
    puntos_venta = relationship("PuntoVenta", back_populates="sucursal")

    __table_args__ = (UniqueConstraint('empresa_id', 'codigo_sucursal_siat', name='uq_empresa_codigo_sucursal'),)

class PuntoVenta(Base):
    __tablename__ = "puntos_venta"
    id = Column(Integer, primary_key=True, index=True)
    sucursal_id = Column(Integer, ForeignKey("sucursales.id"), nullable=False)
    codigo_punto_venta_siat = Column(Integer, nullable=False) # Código 0 si no aplica
    nombre_punto_venta = Column(String(255))
    tipo_punto_venta_siat_id = Column(Integer, ForeignKey("siat_tipos_punto_venta.id"), nullable=False)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

    sucursal = relationship("Sucursal", back_populates="puntos_venta")
    cuis_activos = relationship("Cuis", back_populates="punto_venta") # Podría ser una relación a Cuis activo
    cufd_activos = relationship("Cufd", back_populates="punto_venta") # Podría ser una relación a Cufd activo
    tipo_punto_venta_siat = relationship("TipoPuntoVentaSiat", back_populates="puntos_venta")

    __table_args__ = (UniqueConstraint('sucursal_id', 'codigo_punto_venta_siat', name='uq_sucursal_codigo_punto_venta'),)

class Cuis(Base):
    __tablename__ = "cuis"
    id = Column(Integer, primary_key=True, index=True)
    punto_venta_id = Column(Integer, ForeignKey("puntos_venta.id"), nullable=False)
    codigo_cuis = Column(String(100), unique=True, nullable=False)
    fecha_vigencia = Column(DateTime, nullable=False)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    # No hay actualizado_en porque un CUIS no se modifica, se crea uno nuevo.

    punto_venta = relationship("PuntoVenta", back_populates="cuis_activos")

class Cufd(Base):
    __tablename__ = "cufd"
    id = Column(Integer, primary_key=True, index=True)
    punto_venta_id = Column(Integer, ForeignKey("puntos_venta.id"), nullable=False)
    codigo_cufd = Column(String(100), unique=True, nullable=False) # Ajustado a 100 según XSD factura
    codigo_control = Column(String(50), nullable=False)
    direccion_siat = Column(String(500), nullable=False) # Dirección del servicio SIAT para este CUFD
    fecha_vigencia = Column(DateTime, nullable=False)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())

    punto_venta = relationship("PuntoVenta", back_populates="cufd_activos")

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    codigo_cliente_erp = Column(String(20), unique=True, nullable=False, index=True) 
    numero_documento = Column(String(20), nullable=False, index=True) 
    codigo_tipo_documento_identidad = Column(String(5), ForeignKey("tipos_documento_identidad_siat.codigo_clasificador"), nullable=False) 
    complemento = Column(String(10), nullable=True) 
    nombre_razon_social = Column(String(255), nullable=False)
    email = Column(String(100), nullable=True)
    telefono = Column(String(50), nullable=True)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

    facturas = relationship("Factura", back_populates="cliente")

class Factura(Base):
    __tablename__ = "facturas"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    punto_venta_id = Column(Integer, ForeignKey("puntos_venta.id"), nullable=False)
    cufd_id = Column(Integer, ForeignKey("cufd.id"), nullable=False) 
    
    numero_factura = Column(Integer, nullable=False)
    cuf = Column(String(100), unique=True, nullable=False, index=True) 
    fecha_emision = Column(DateTime, nullable=False, default=func.now())
    
    monto_total = Column(Numeric(17, 2), nullable=False)
    monto_descuento = Column(Numeric(17, 2), nullable=True, default=0.0) 
    monto_gift_card = Column(Numeric(17, 2), nullable=True, default=0.0)
    monto_total_sujeto_iva = Column(Numeric(17, 2), nullable=False)
    
    codigo_metodo_pago_siat_id = Column(Integer, ForeignKey("siat_tipos_metodo_pago.id"), nullable=False) 
    numero_tarjeta = Column(String(16), nullable=True) 
    
    codigo_moneda_siat_id = Column(Integer, ForeignKey("siat_tipos_moneda.id"), nullable=False, default="1") # Asumiendo "1" para Boliviano
    tipo_cambio = Column(Numeric(17, 2), nullable=False, default=1.0)
    
    leyenda = Column(String(500), nullable=False)
    usuario_emisor = Column(String(100), nullable=False)
    codigo_documento_sector_siat_id = Column(Integer, ForeignKey("siat_tipos_documento_sector.id"), nullable=False) # Ajustar si el nombre de la tabla es diferente
    
    codigo_tipo_factura_siat_id = Column(Integer, ForeignKey("siat_tipos_factura.id"), nullable=False, default="1") # Asumiendo "1"
    codigo_tipo_emision_siat_id = Column(Integer, ForeignKey("siat_tipos_emision.id"), nullable=False, default="1") # Asumiendo "1" Online
    
    cafc = Column(String(50), nullable=True)
    codigo_excepcion_siat = Column(Integer, nullable=True) # Este parece ser un código de estado numérico, no un clasificador. Mantener como Integer.

    xml_generado = Column(Text, nullable=True)
    xml_firmado_enviado = Column(Text, nullable=True)
    hash_xml_enviado = Column(String(64), nullable=True) 
    fecha_envio_siat = Column(DateTime, nullable=True)

    respuesta_siat = Column(Text, nullable=True)
    codigo_estado_siat = Column(String(50), nullable=True) # Este es un código de estado, usualmente numérico pero puede ser string.
    
    anulada = Column(Boolean, default=False)
    fecha_anulacion = Column(DateTime, nullable=True)
    codigo_motivo_anulacion_siat_id = Column(Integer, ForeignKey("siat_tipos_motivo_anulacion.id"), nullable=True)

    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

    cliente = relationship("Cliente", back_populates="facturas")
    punto_venta = relationship("PuntoVenta") 
    cufd_usado = relationship("Cufd") 
    detalles = relationship("DetalleFactura", back_populates="factura", cascade="all, delete-orphan")

    __table_args__ = (UniqueConstraint('punto_venta_id', 'numero_factura', 'cufd_id', name='uq_pv_numfact_cufd'),)


class DetalleFactura(Base):
    __tablename__ = "detalles_factura"
    id = Column(Integer, primary_key=True, index=True)
    factura_id = Column(Integer, ForeignKey("facturas.id"), nullable=False)
    
    actividad_economica_siat = Column(String(10), ForeignKey("actividades_economicas_siat.codigo_clasificador"), nullable=False) 
    codigo_producto_sin_siat = Column(Integer, nullable=False) # Código SIN, parece ser numérico.
    codigo_producto_empresa = Column(String(50), nullable=False)
    descripcion = Column(String(500), nullable=False)
    
    cantidad = Column(Numeric(17, 5), nullable=False) 
    unidad_medida_siat_id = Column(Integer, ForeignKey("siat_unidades_medida.id"), nullable=False) 
    precio_unitario = Column(Numeric(17, 2), nullable=False)
    monto_descuento_detalle = Column(Numeric(17, 2), nullable=True, default=0.0)
    subtotal = Column(Numeric(17, 2), nullable=False)
    
    numero_serie = Column(String(1500), nullable=True) # Ajustado a String(1500) según XSD
    numero_imei = Column(String(1500), nullable=True) # Ajustado a String(1500) según XSD
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

    factura = relationship("Factura", back_populates="detalles")
    producto_servicio_siat = relationship("ProductoServicioSiat", back_populates="detalles_factura")
    unidad_medida_siat = relationship("UnidadMedidaSiat") # Asumiendo que UnidadMedidaSiat no necesita back_populates="detalles_factura"
    # tipo_habitacion_siat = relationship("TipoHabitacionSiat", back_populates="detalles_factura") # Si aplica


class EventoContingencia(Base):
    __tablename__ = "eventos_contingencia"
    id = Column(Integer, primary_key=True, index=True)
    punto_venta_id = Column(Integer, ForeignKey("puntos_venta.id"), nullable=False)
    codigo_evento_siat_id = Column(Integer, ForeignKey("siat_tipos_evento_significativo.id"), nullable=False)
    codigo_motivo_evento_siat = Column(String(50), nullable=False) # Según catálogo del SIAT
    descripcion_evento = Column(String(500), nullable=False)
    fecha_hora_inicio_evento = Column(DateTime, nullable=False)
    fecha_hora_fin_evento = Column(DateTime, nullable=True)
    cufd_evento_contingencia = Column(String(255), nullable=False) # CUFD utilizado durante la contingencia
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

    punto_venta = relationship("PuntoVenta") # Relación simple
    tipo_evento_significativo_siat = relationship("TipoEventoSignificativoSiat", back_populates="eventos_contingencia")

# Modelos de Catálogos SIAT (Sincronización)

class TipoDocumentoIdentidadSiat(Base):
    __tablename__ = "tipos_documento_identidad_siat"
    id = Column(Integer, primary_key=True, index=True)
    codigo_clasificador = Column(String(5), unique=True, nullable=False, index=True)
    descripcion = Column(String(255), nullable=False)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

class MetodoPagoSiat(Base):
    __tablename__ = "metodos_pago_siat"
    id = Column(Integer, primary_key=True, index=True)
    codigo_clasificador = Column(String(10), unique=True, nullable=False, index=True)
    descripcion = Column(String(255), nullable=False)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

class TipoMonedaSiat(Base):
    __tablename__ = "tipos_moneda_siat"
    id = Column(Integer, primary_key=True, index=True)
    codigo_clasificador = Column(String(5), unique=True, nullable=False, index=True)
    descripcion = Column(String(255), nullable=False)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

class DocumentoSectorSiat(Base):
    __tablename__ = "documentos_sector_siat"
    id = Column(Integer, primary_key=True, index=True)
    codigo_clasificador = Column(String(5), unique=True, nullable=False, index=True)
    descripcion = Column(String(255), nullable=False)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

class TipoFacturaSiat(Base):
    __tablename__ = "tipos_factura_siat"
    id = Column(Integer, primary_key=True, index=True)
    codigo_clasificador = Column(String(5), unique=True, nullable=False, index=True)
    descripcion = Column(String(255), nullable=False)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

class TipoEmisionSiat(Base):
    __tablename__ = "tipos_emision_siat"
    id = Column(Integer, primary_key=True, index=True)
    codigo_clasificador = Column(String(10), unique=True, nullable=False, index=True)
    descripcion = Column(String(255), nullable=False)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

class MotivoAnulacionSiat(Base):
    __tablename__ = "motivos_anulacion_siat"
    id = Column(Integer, primary_key=True, index=True)
    codigo_clasificador = Column(String(10), unique=True, nullable=False, index=True)
    descripcion = Column(String(255), nullable=False)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

class ActividadEconomicaSiat(Base):
    __tablename__ = "actividades_economicas_siat"
    id = Column(Integer, primary_key=True, index=True)
    codigo_clasificador = Column(String(10), unique=True, nullable=False, index=True) # CAEB puede ser más largo, ajustar si es necesario
    descripcion = Column(String(500), nullable=False)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

class UnidadMedidaSiat(Base):
    __tablename__ = "unidades_medida_siat"
    id = Column(Integer, primary_key=True, index=True)
    codigo_clasificador = Column(String(5), unique=True, nullable=False, index=True)
    descripcion = Column(String(255), nullable=False)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

class TipoPuntoVentaSiat(Base):
    __tablename__ = "siat_tipos_punto_venta"
    __table_args__ = (UniqueConstraint('codigo_clasificador', name='uq_siat_tipos_punto_venta_codigo_clasificador'),)

    id = Column(Integer, primary_key=True, index=True)
    codigo_clasificador = Column(String(10), nullable=False, unique=True) # Código Asignado por el SIAT
    descripcion = Column(String(255), nullable=False)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())
    # Relación con PuntoVenta
    puntos_venta = relationship("PuntoVenta", back_populates="tipo_punto_venta_siat")

class TipoHabitacionSiat(Base):
    __tablename__ = "siat_tipos_habitacion"
    __table_args__ = (UniqueConstraint('codigo_clasificador', name='uq_siat_tipos_habitacion_codigo_clasificador'),)

    id = Column(Integer, primary_key=True, index=True)
    codigo_clasificador = Column(String(10), nullable=False, unique=True) # Código Asignado por el SIAT
    descripcion = Column(String(255), nullable=False)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())
    # Relación (si aplica, por ejemplo, con DetalleFactura para servicios de hotel)
    # detalles_factura = relationship("DetalleFactura", back_populates="tipo_habitacion_siat")


class LeyendaFacturaSiat(Base):
    __tablename__ = "siat_leyendas_factura"
    # No hay un 'codigo_clasificador' único directo en la tabla de referencia, se usa ID autoincremental
    # y se podría añadir una restricción de unicidad sobre 'codigo_actividad' y 'descripcion_leyenda' si se considera necesario.
    # __table_args__ = (UniqueConstraint('codigo_actividad', 'descripcion_leyenda', name='uq_siat_leyendas_factura_actividad_desc'),)

    id = Column(Integer, primary_key=True, index=True)
    codigo_actividad = Column(String(255), nullable=False) # Código de Actividad Económica
    descripcion_leyenda = Column(String(500), nullable=False) # Descripción de la Leyenda
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())
    # Relación con Factura (una factura puede tener una leyenda)
    # facturas = relationship("Factura", back_populates="leyenda_factura_siat") # Se manejará por el campo leyenda en Factura

class ProductoServicioSiat(Base):
    __tablename__ = "siat_productos_servicios"
    __table_args__ = (UniqueConstraint('codigo_actividad', 'codigo_producto', name='uq_siat_productos_servicios_act_prod'),)

    id = Column(Integer, primary_key=True, index=True)
    codigo_actividad = Column(String(20), nullable=False) # Código de Actividad Económica
    codigo_producto = Column(String(20), nullable=False) # Código de Producto Asignado por el SIAT
    descripcion_producto = Column(String(255), nullable=False)
    nandina = Column(Text, nullable=True) # Código Nandina (opcional)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())
    # Relación con DetalleFactura
    detalles_factura = relationship("DetalleFactura", back_populates="producto_servicio_siat")

class TipoEventoSignificativoSiat(Base):
    __tablename__ = "siat_tipos_evento_significativo"
    __table_args__ = (UniqueConstraint('codigo_clasificador', name='uq_siat_tipos_evento_significativo_codigo_clasificador'),)

    id = Column(Integer, primary_key=True, index=True)
    codigo_clasificador = Column(String(10), nullable=False, unique=True) # Código Asignado por el SIAT
    descripcion = Column(String(255), nullable=False)
    # Timestamps
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())
    # Relación con EventoContingencia
    eventos_contingencia = relationship("EventoContingencia", back_populates="tipo_evento_significativo_siat")

class PaisOrigenSiat(Base):
    __tablename__ = "siat_paises_origen"
    __table_args__ = (UniqueConstraint('codigo_clasificador', name='uq_siat_paises_origen_codigo_clasificador'),)

    id = Column(Integer, primary_key=True, index=True)
    codigo_clasificador = Column(String(10), nullable=False, unique=True)
    descripcion = Column(String(255), nullable=False)
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

class ActividadDocumentoSectorSiat(Base):
    __tablename__ = "siat_actividades_documento_sector"
    __table_args__ = (UniqueConstraint('codigo_actividad', 'codigo_documento_sector', name='uq_siat_act_doc_sec_ca_cds'),)

    id = Column(Integer, primary_key=True, index=True)
    codigo_actividad = Column(String(10), nullable=False)
    codigo_documento_sector = Column(Integer, nullable=False) # En la tabla de referencia es INT
    tipo_documento_sector = Column(String(255))
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

class MensajeServicioSiat(Base):
    __tablename__ = "siat_mensajes_servicio"
    __table_args__ = (UniqueConstraint('codigo_clasificador', name='uq_siat_mensajes_servicio_codigo_clasificador'),)

    id = Column(Integer, primary_key=True, index=True)
    codigo_clasificador = Column(String(10), nullable=False, unique=True)
    descripcion = Column(String(255), nullable=False)
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

class ActividadSiat(Base):
    __tablename__ = "siat_actividades"
    __table_args__ = (UniqueConstraint('codigo_caeb', name='uq_siat_actividades_codigo_caeb'),)

    id = Column(Integer, primary_key=True, index=True)
    codigo_caeb = Column(String(10), nullable=False, unique=True) # Código CAEB (Clasificador de Actividades Económicas de Bolivia)
    descripcion = Column(String(255), nullable=False)
    tipo_actividad = Column(String(255)) # EJ: P (Principal), S (Secundaria)
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

# La configuración del motor y la sesión se maneja en database_manager.py y Alembic.
# No es necesario configurar engine o SessionLocal aquí.
# Base.metadata.create_all(bind=engine) # Esto se manejará con Alembic
