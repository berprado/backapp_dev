from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LeyendaFacturaSiatBase(BaseModel):
    codigo_actividad: str
    descripcion_leyenda: str

class LeyendaFacturaSiatCreate(LeyendaFacturaSiatBase):
    pass

class LeyendaFacturaSiatUpdate(LeyendaFacturaSiatBase):
    pass

class LeyendaFacturaSiatSchema(LeyendaFacturaSiatBase):
    id: int
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    class Config:
        orm_mode = True
