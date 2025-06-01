from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

# Esquema base con los campos comunes.
class ClienteBase(BaseModel):
    codigo_cliente: str = Field(description="Identificador único del cliente (NIT, CI, CEX, etc.)")
    nombre_razon_social: str = Field(description="Nombre o razón social del cliente")
    email: Optional[EmailStr] = Field(default=None, description="Correo electrónico del cliente")
    telefono: Optional[str] = Field(default=None, description="Número de teléfono del cliente")
    complemento_ci: Optional[str] = Field(default=None, description="Complemento del CI, si aplica")

# Esquema para la creación de un cliente.
class ClienteCreate(ClienteBase):
    # Todos los campos necesarios para crear un cliente ya están en ClienteBase.
    # Si algún campo opcional en ClienteBase fuera obligatorio en la creación,
    # se redefiniría aquí. Por ejemplo:
    # email: EmailStr # Si el email fuera obligatorio al crear
    pass

# Esquema para la actualización de un cliente.
# Todos los campos son opcionales.
class ClienteUpdate(BaseModel):
    codigo_cliente: Optional[str] = Field(default=None, description="Nuevo identificador único del cliente (raramente se cambia)")
    nombre_razon_social: Optional[str] = Field(default=None, description="Nuevo nombre o razón social del cliente")
    email: Optional[EmailStr] = Field(default=None, description="Nuevo correo electrónico del cliente")
    telefono: Optional[str] = Field(default=None, description="Nuevo número de teléfono del cliente")
    complemento_ci: Optional[str] = Field(default=None, description="Nuevo complemento del CI")

# Esquema para representar un cliente leído desde la base de datos.
class ClienteInDB(ClienteBase):
    id: int
    creado_en: datetime
    actualizado_en: datetime

    class Config:
        from_attributes = True

# Esquema principal para devolver información de clientes.
class Cliente(ClienteInDB):
    pass
