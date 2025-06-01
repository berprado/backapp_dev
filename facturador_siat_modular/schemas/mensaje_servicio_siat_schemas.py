from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MensajeServicioSiatBase(BaseModel):
    codigo_clasificador: str
    descripcion: str

class MensajeServicioSiatCreate(MensajeServicioSiatBase):
    pass

class MensajeServicioSiatUpdate(MensajeServicioSiatBase):
    pass

class MensajeServicioSiatSchema(MensajeServicioSiatBase):
    id: int
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    class Config:
        orm_mode = True
