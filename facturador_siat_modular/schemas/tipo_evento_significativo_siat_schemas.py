from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TipoEventoSignificativoSiatBase(BaseModel):
    codigo_clasificador: str
    descripcion: str

class TipoEventoSignificativoSiatCreate(TipoEventoSignificativoSiatBase):
    pass

class TipoEventoSignificativoSiatUpdate(TipoEventoSignificativoSiatBase):
    pass

class TipoEventoSignificativoSiatSchema(TipoEventoSignificativoSiatBase):
    id: int
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    class Config:
        orm_mode = True
