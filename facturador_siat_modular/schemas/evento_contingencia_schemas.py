from pydantic import BaseModel, Field
from typing import Optional
import datetime

class EventoContingenciaBase(BaseModel):
    punto_venta_id: int
    codigo_evento_siat: Optional[str] = Field(None, max_length=100) # Puede ser None inicialmente
    codigo_motivo_evento_siat: str = Field(..., max_length=50)
    descripcion_evento: str = Field(..., max_length=500)
    fecha_hora_inicio_evento: datetime.datetime
    fecha_hora_fin_evento: Optional[datetime.datetime] = None
    cufd_evento_contingencia: str = Field(..., max_length=255)

class EventoContingenciaCreate(EventoContingenciaBase):
    pass # No hay campos adicionales para la creación más allá de la base

class EventoContingenciaUpdate(BaseModel):
    punto_venta_id: Optional[int] = None
    codigo_evento_siat: Optional[str] = Field(None, max_length=100)
    codigo_motivo_evento_siat: Optional[str] = Field(None, max_length=50)
    descripcion_evento: Optional[str] = Field(None, max_length=500)
    fecha_hora_inicio_evento: Optional[datetime.datetime] = None
    # fecha_hora_fin_evento ya es Optional en Base, se mantiene
    fecha_hora_fin_evento: Optional[datetime.datetime] = None
    cufd_evento_contingencia: Optional[str] = Field(None, max_length=255)

    class Config:
        # from_attributes = True # Pydantic V2
        orm_mode = True # Para compatibilidad si se usa Pydantic V1 en algún lugar, aunque from_attributes es V2

class EventoContingenciaSchema(EventoContingenciaBase):
    id: int
    creado_en: Optional[datetime.datetime] = None
    actualizado_en: Optional[datetime.datetime] = None

    class Config:
        orm_mode = True
        # from_attributes = True # En Pydantic V2, orm_mode es ahora from_attributes
