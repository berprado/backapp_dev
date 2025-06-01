# C:\Users\Bernardo\Desktop\backapp_dev\facturador_siat_modular\schemas\empresa_schemas.py

from typing import Optional
from datetime import datetime
from pydantic import BaseModel
# Esquema base con los campos comunes que se esperan al crear o que están en la BD.
class EmpresaBase(BaseModel):
    nit: str
    razon_social: str

# Esquema para la creación de una empresa.
# Hereda de EmpresaBase, no necesita campos adicionales para la creación simple.
class EmpresaCreate(EmpresaBase):
    pass

# Esquema para la actualización de una empresa.
# Todos los campos son opcionales, ya que se puede actualizar solo uno o varios.
class EmpresaUpdate(BaseModel):
    nit: Optional[str] = None
    razon_social: Optional[str] = None

# Esquema para representar una empresa tal como se lee desde la base de datos.
# Incluye campos que son generados por la BD (id, creado_en, actualizado_en).
class EmpresaInDB(EmpresaBase):
    id: int
    creado_en: datetime
    actualizado_en: datetime

    class Config:
        from_attributes = True # Para Pydantic v2. En Pydantic v1 era orm_mode = True

# Podríamos añadir un esquema más general para devolver empresas al cliente,
# que podría ser igual a EmpresaInDB o tener menos campos si fuera necesario.
class Empresa(EmpresaInDB):
    pass
