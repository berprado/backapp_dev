# C:\Users\Bernardo\Desktop\backapp_dev\facturador_siat_modular\schemas\punto_venta_schemas.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Esquema base con los campos comunes.
class PuntoVentaBase(BaseModel):
    sucursal_id: int = Field(gt=0, description="El ID de la sucursal a la que pertenece el punto de venta")
    codigo_punto_venta_siat: int = Field(description="Código de punto de venta asignado por el SIAT (0 si no aplica o es el único)")
    nombre_punto_venta: Optional[str] = None
    tipo_punto_venta_siat: Optional[str] = None # Según catálogos del SIAT

# Esquema para la creación de un punto de venta.
class PuntoVentaCreate(PuntoVentaBase):
    # 'nombre_punto_venta' podría ser obligatorio en la creación, si así se decide.
    # Ejemplo: nombre_punto_venta: str
    pass

# Esquema para la actualización de un punto de venta.
# Todos los campos son opcionales.
class PuntoVentaUpdate(BaseModel):
    sucursal_id: Optional[int] = Field(default=None, gt=0, description="El ID de la sucursal (raramente se cambia)")
    codigo_punto_venta_siat: Optional[int] = Field(default=None, description="Código de punto de venta SIAT")
    nombre_punto_venta: Optional[str] = None
    tipo_punto_venta_siat: Optional[str] = None

# Esquema para representar un punto de venta leído desde la base de datos.
class PuntoVentaInDB(PuntoVentaBase):
    id: int
    creado_en: datetime
    actualizado_en: datetime

    class Config:
        from_attributes = True

# Esquema principal para devolver puntos de venta.
class PuntoVenta(PuntoVentaInDB):
    pass
