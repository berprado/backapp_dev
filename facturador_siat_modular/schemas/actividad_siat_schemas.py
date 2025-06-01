from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ActividadSiatBase(BaseModel):
    codigo_caeb: str
    descripcion: str
    tipo_actividad: Optional[str] = None

class ActividadSiatCreate(ActividadSiatBase):
    pass

class ActividadSiatUpdate(BaseModel):
    codigo_caeb: Optional[str] = None
    descripcion: Optional[str] = None
    tipo_actividad: Optional[str] = None

class ActividadSiatSchema(ActividadSiatBase):
    id: int
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    class Config:
        orm_mode = True
