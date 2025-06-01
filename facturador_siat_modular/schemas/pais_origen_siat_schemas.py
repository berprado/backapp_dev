from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PaisOrigenSiatBase(BaseModel):
    codigo_clasificador: str
    descripcion: str

class PaisOrigenSiatCreate(PaisOrigenSiatBase):
    pass

class PaisOrigenSiatUpdate(BaseModel):
    codigo_clasificador: Optional[str] = None
    descripcion: Optional[str] = None

class PaisOrigenSiatSchema(PaisOrigenSiatBase):
    id: int
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    class Config:
        orm_mode = True
