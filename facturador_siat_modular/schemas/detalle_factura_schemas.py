from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal
import datetime

class DetalleFacturaBase(BaseModel):
    actividad_economica_siat: str = Field(..., max_length=10)
    codigo_producto_sin_siat: int
    codigo_producto_empresa: str = Field(..., max_length=50)
    descripcion: str = Field(..., max_length=500)
    cantidad: Decimal = Field(..., max_digits=17, decimal_places=5)
    unidad_medida_siat: str = Field(..., max_length=5)
    precio_unitario: Decimal = Field(..., max_digits=17, decimal_places=2)
    monto_descuento_detalle: Optional[Decimal] = Field(None, max_digits=17, decimal_places=2)
    subtotal: Decimal = Field(..., max_digits=17, decimal_places=2)
    numero_serie: Optional[str] = Field(None, max_length=1500)
    numero_imei: Optional[str] = Field(None, max_length=1500)

class DetalleFacturaCreate(DetalleFacturaBase):
    pass

class DetalleFacturaUpdate(BaseModel):
    factura_id: Optional[int] = None
    producto_id: Optional[int] = None # Asumiendo que tienes un modelo Producto y su ID
    codigo_producto_siat: Optional[str] = Field(None, max_length=20)
    descripcion: Optional[str] = Field(None, max_length=255)
    cantidad: Optional[Decimal] = None # type: ignore
    unidad_medida_siat: Optional[str] = Field(None, max_length=10)
    precio_unitario: Optional[Decimal] = None # type: ignore
    monto_descuento: Optional[Decimal] = None # type: ignore
    subtotal: Optional[Decimal] = None # type: ignore
    numero_serie: Optional[str] = Field(None, max_length=255)
    numero_imei: Optional[str] = Field(None, max_length=255)
    actividad_economica_siat: Optional[str] = Field(None, max_length=20) # Código de Actividad Económica

    class Config:
        from_attributes = True # Pydantic V2
        # orm_mode = True # Pydantic V1

class DetalleFacturaSchema(DetalleFacturaBase):
    id: int
    factura_id: int
    creado_en: Optional[datetime.datetime] = None
    actualizado_en: Optional[datetime.datetime] = None

    class Config:
        orm_mode = True
        # from_attributes = True # En Pydantic V2, orm_mode es ahora from_attributes
