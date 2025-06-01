\
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TipoPuntoVentaSiatBase(BaseModel):
    codigo_clasificador: str
    descripcion: str

class TipoPuntoVentaSiatCreate(TipoPuntoVentaSiatBase):
    pass

class TipoPuntoVentaSiatUpdate(TipoPuntoVentaSiatBase):
    pass

class TipoPuntoVentaSiatSchema(TipoPuntoVentaSiatBase):
    id: int
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    class Config:
        orm_mode = True
