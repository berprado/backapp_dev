'''
Este módulo define los esquemas Pydantic para la gestión de CUFDs (Código Único de Facturación Diaria).
'''
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# Esquema base con los campos que coinciden con el modelo SQLAlchemy Cufd
class CufdBase(BaseModel):
    punto_venta_id: int = Field(description="ID del punto de venta asociado a este CUFD.")
    codigo_cufd: str = Field(max_length=255, description="Código CUFD proporcionado por el SIAT.")
    codigo_control: str = Field(max_length=50, description="Código de control asociado al CUFD.")
    direccion_siat: str = Field(max_length=500, description="Dirección del servicio SIAT para este CUFD.")
    fecha_vigencia: datetime = Field(description="Fecha y hora hasta la cual el CUFD es válido.")

# Esquema para la creación de un CUFD.
# Hereda todos los campos de CufdBase, que ya son obligatorios.
class CufdCreate(CufdBase):
    pass

# Esquema para la actualización de un CUFD.
# Generalmente, los CUFD no se actualizan; se crea uno nuevo.
# Pero si se permitiera, todos los campos serían opcionales.
class CufdUpdate(BaseModel):
    punto_venta_id: Optional[int] = Field(default=None, description="ID del punto de venta asociado a este CUFD.")
    codigo_cufd: Optional[str] = Field(default=None, max_length=255, description="Código CUFD proporcionado por el SIAT.")
    codigo_control: Optional[str] = Field(default=None, max_length=50, description="Código de control asociado al CUFD.")
    direccion_siat: Optional[str] = Field(default=None, max_length=500, description="Dirección del servicio SIAT para este CUFD.")
    fecha_vigencia: Optional[datetime] = Field(default=None, description="Fecha y hora hasta la cual el CUFD es válido.")

# Esquema para representar un CUFD leído desde la base de datos.
class CufdInDB(CufdBase):
    id: int  # Coincide con el 'id' del modelo SQLAlchemy
    creado_en: datetime # Coincide con 'creado_en' del modelo SQLAlchemy
    # El modelo Cufd no tiene 'actualizado_en'

    class Config:
        from_attributes = True # Cambiado de orm_mode
        # allow_population_by_field_name ya no es necesario si los nombres coinciden
        schema_extra = { # Actualizado para reflejar los nuevos nombres de campo
            "example": {
                "id": 1,
                "punto_venta_id": 1,
                "codigo_cufd": "ABCDEF0123456789",
                "codigo_control": "XYZ987",
                "direccion_siat": "https://pilotosiat.impuestos.gob.bo/ServicioFacturacion...",
                "fecha_vigencia": "2025-06-01T23:59:59",
                "creado_en": "2025-06-01T10:00:00"
            }
        }

# Esquema principal para devolver información de CUFDs.
class Cufd(CufdInDB):
    pass
