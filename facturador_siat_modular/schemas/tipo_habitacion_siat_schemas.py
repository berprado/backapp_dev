from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TipoHabitacionSiatBase(BaseModel):
    codigo_clasificador: str
    descripcion: str

class TipoHabitacionSiatCreate(TipoHabitacionSiatBase):
    pass

class TipoHabitacionSiatUpdate(TipoHabitacionSiatBase):
    pass

class TipoHabitacionSiatSchema(TipoHabitacionSiatBase):
    id: int
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    class Config:
        orm_mode = True
