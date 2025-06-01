from pydantic import BaseModel, Field
from typing import Optional, List
from decimal import Decimal
import datetime
from .detalle_factura_schemas import DetalleFacturaCreate, DetalleFacturaSchema # Importamos los esquemas de detalle

class FacturaBase(BaseModel):
    cliente_id: int
    punto_venta_id: int
    cufd_id: int
    numero_factura: int
    cuf: str = Field(..., max_length=100)
    fecha_emision: datetime.datetime = Field(default_factory=datetime.datetime.now)
    monto_total: Decimal = Field(..., max_digits=17, decimal_places=2)
    monto_descuento: Optional[Decimal] = Field(None, max_digits=17, decimal_places=2)
    monto_gift_card: Optional[Decimal] = Field(None, max_digits=17, decimal_places=2)
    monto_total_sujeto_iva: Decimal = Field(..., max_digits=17, decimal_places=2)
    codigo_metodo_pago_siat: str = Field(..., max_length=10)
    numero_tarjeta: Optional[str] = Field(None, max_length=16)
    codigo_moneda_siat: str = Field(..., max_length=5)
    tipo_cambio: Decimal = Field(..., max_digits=17, decimal_places=2)
    leyenda: str = Field(..., max_length=500)
    usuario_emisor: str = Field(..., max_length=100)
    codigo_documento_sector: str = Field(..., max_length=5)
    codigo_tipo_factura_siat: str = Field(..., max_length=5)
    codigo_tipo_emision_siat: str = Field(..., max_length=10)
    cafc: Optional[str] = Field(None, max_length=50)
    codigo_excepcion_siat: Optional[int] = None
    xml_generado: Optional[str] = None
    xml_firmado_enviado: Optional[str] = None
    hash_xml_enviado: Optional[str] = Field(None, max_length=64)
    fecha_envio_siat: Optional[datetime.datetime] = None
    respuesta_siat: Optional[str] = None
    codigo_estado_siat: Optional[str] = Field(None, max_length=50)
    anulada: Optional[bool] = False
    fecha_anulacion: Optional[datetime.datetime] = None
    codigo_motivo_anulacion_siat: Optional[str] = Field(None, max_length=10)

class FacturaCreate(FacturaBase):
    detalles: List[DetalleFacturaCreate] = []

class FacturaUpdate(BaseModel):
    cliente_id: Optional[int] = None
    sucursal_id: Optional[int] = None
    punto_venta_id: Optional[int] = None
    cufd_id: Optional[int] = None
    codigo_metodo_pago_siat: Optional[str] = Field(None, max_length=10)
    codigo_moneda_siat: Optional[str] = Field(None, max_length=5)
    tipo_cambio: Optional[Decimal] = None # type: ignore
    numero_factura_siat: Optional[int] = None
    fecha_emision: Optional[datetime.datetime] = None
    nombre_razon_social: Optional[str] = Field(None, max_length=255)
    codigo_tipo_documento_identidad_siat: Optional[str] = Field(None, max_length=5)
    numero_documento: Optional[str] = Field(None, max_length=50)
    complemento: Optional[str] = Field(None, max_length=50)
    codigo_cliente: Optional[str] = Field(None, max_length=100)
    monto_total: Optional[Decimal] = None # type: ignore
    monto_total_sujeto_iva: Optional[Decimal] = None # type: ignore
    monto_gift_card: Optional[Decimal] = None # type: ignore
    descuento_adicional: Optional[Decimal] = None # type: ignore
    codigo_excepcion_documento: Optional[int] = None
    cafc: Optional[str] = Field(None, max_length=100) 
    leyenda: Optional[str] = Field(None, max_length=500)
    usuario: Optional[str] = Field(None, max_length=100)
    codigo_documento_sector_siat: Optional[str] = Field(None, max_length=5)
    # Campos de respuesta SIAT
    codigo_recepcion_siat: Optional[str] = Field(None, max_length=255)
    estado_factura_siat: Optional[str] = Field(None, max_length=50) # EJ: VALIDADA, RECHAZADA, OBSERVADA, ANULADA
    cuf: Optional[str] = Field(None, max_length=255)
    url_sin: Optional[str] = Field(None, max_length=500)
    # Campos de control
    procesado: Optional[bool] = False
    error_procesamiento: Optional[str] = Field(None, max_length=1000)
    xml_generado: Optional[str] = None
    # Relaciones
    # detalles: Optional[List["DetalleFacturaSchema"]] = [] # Se maneja por separado

    class Config:
        from_attributes = True # Pydantic V2
        # orm_mode = True # Pydantic V1

class FacturaSchema(FacturaBase):
    id: int
    creado_en: Optional[datetime.datetime] = None
    actualizado_en: Optional[datetime.datetime] = None
    detalles: List[DetalleFacturaSchema] = []

    class Config:
        orm_mode = True
        # from_attributes = True # En Pydantic V2, orm_mode es ahora from_attributes
