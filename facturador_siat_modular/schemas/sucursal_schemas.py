# C:\Users\Bernardo\Desktop\backapp_dev\facturador_siat_modular\schemas\sucursal_schemas.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Esquema base con los campos comunes.
class SucursalBase(BaseModel):
    empresa_id: int = Field(gt=0, description="El ID de la empresa a la que pertenece la sucursal")
    codigo_sucursal_siat: int = Field(description="Código de sucursal asignado por el SIAT (0 para Casa Matriz)")
    descripcion: Optional[str] = None  # Campo del modelo SQLAlchemy
    direccion: Optional[str] = None    # Campo del modelo SQLAlchemy

# Esquema para la creación de una sucursal.
# Hereda de SucursalBase. Los campos opcionales en SucursalBase lo serán también aquí.
# Si 'descripcion' o 'direccion' fueran obligatorios en la creación, se podrían redefinir aquí.
class SucursalCreate(SucursalBase):
    # Para la creación, 'empresa_id' y 'codigo_sucursal_siat' son esenciales.
    # 'descripcion' y 'direccion' pueden ser opcionales según el modelo.
    pass

# Esquema para la actualización de una sucursal.
# Todos los campos son opcionales.
class SucursalUpdate(BaseModel):
    empresa_id: Optional[int] = Field(default=None, gt=0, description="El ID de la empresa (no se suele cambiar, pero se permite)")
    codigo_sucursal_siat: Optional[int] = Field(default=None, description="Código de sucursal SIAT")
    descripcion: Optional[str] = None
    direccion: Optional[str] = None

# Esquema para representar una sucursal leída desde la base de datos.
class SucursalInDB(SucursalBase):
    id: int
    creado_en: datetime
    actualizado_en: datetime

    class Config:
        from_attributes = True

# Esquema principal para devolver sucursales.
class Sucursal(SucursalInDB):
    pass
