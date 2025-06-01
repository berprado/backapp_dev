from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ActividadDocumentoSectorSiatBase(BaseModel):
    codigo_actividad: str
    codigo_documento_sector: int
    tipo_documento_sector: Optional[str] = None

class ActividadDocumentoSectorSiatCreate(ActividadDocumentoSectorSiatBase):
    pass

class ActividadDocumentoSectorSiatUpdate(BaseModel):
    codigo_actividad: Optional[str] = None
    codigo_documento_sector: Optional[int] = None
    tipo_documento_sector: Optional[str] = None

class ActividadDocumentoSectorSiatSchema(ActividadDocumentoSectorSiatBase):
    id: int
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    class Config:
        orm_mode = True
