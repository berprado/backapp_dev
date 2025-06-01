from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime

class ProductoServicioSiatBase(BaseModel):
    codigo_actividad: str
    codigo_producto: str
    descripcion_producto: str
    nandina: Optional[Text] = None

class ProductoServicioSiatCreate(ProductoServicioSiatBase):
    pass

class ProductoServicioSiatUpdate(ProductoServicioSiatBase):
    pass

class ProductoServicioSiatSchema(ProductoServicioSiatBase):
    id: int
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    class Config:
        orm_mode = True
