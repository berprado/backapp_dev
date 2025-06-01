from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..config import config
from .models import Base  # Importar Base desde .models
import logging
from typing import Any, Dict, Generic, List, Type, TypeVar, Union # <--- Añadido
from pydantic import BaseModel # <--- Añadido

logger = logging.getLogger(__name__)

DATABASE_URL = config.DATABASE_URL
engine = None
SessionLocal = None

if DATABASE_URL:
    try:
        # Se elimina echo=config.DB_ECHO_LOG por ahora.
        engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        logger.info(f"Motor de base de datos SQLAlchemy inicializado para: {DATABASE_URL}")
    except ImportError as ie:
        logger.error(f"Error de importación al inicializar SQLAlchemy (¿Falta mysqlclient?): {ie}")
        engine = None
        SessionLocal = None
    except Exception as e:
        logger.error(f"Error al crear el motor de base de datos SQLAlchemy: {e}")
        engine = None
        SessionLocal = None
else:
    logger.warning("DATABASE_URL no está configurada en el archivo .env. El sistema de base de datos no estará disponible.")

def init_db():
    """
    Inicializa la base de datos creando todas las tablas definidas en los modelos.
    PRECAUCIÓN: En un entorno de producción, Alembic debería usarse para manejar las migraciones.
    Esta función es más adecuada para desarrollo o pruebas iniciales.
    """
    if not engine:
        logger.error("El motor de la base de datos (engine) no está inicializado. No se pueden crear las tablas.")
        return
    try:
        logger.info("Intentando crear tablas en la base de datos (si no existen)...")
        Base.metadata.create_all(bind=engine)
        logger.info("Tablas verificadas/creadas exitosamente.")
    except Exception as e:
        logger.error(f"Error al crear las tablas en la base de datos: {e}")

def get_db():
    """
    Generador de dependencias para obtener una sesión de base de datos.
    Asegura que la sesión se cierre después de su uso.
    """
    if not SessionLocal:
        logger.error("SessionLocal no está inicializada. No se puede obtener una sesión de BD.")
        return None

    db: Session = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Error durante la sesión de base de datos: {e}")
        db.rollback()
        raise
    finally:
        db.close()
        logger.debug("Sesión de base de datos cerrada.")

# Definición de Tipos Genéricos para el CRUDManager
ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDManager(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        Manager CRUD genérico con operaciones por defecto.

        :param model: Un modelo SQLAlchemy
        """
        self.model = model

    def get(self, db: Session, id: Any) -> ModelType | None:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        # Asumiendo Pydantic v2+, usar model_dump(). Para v1, sería obj_in.dict().
        obj_in_data = obj_in.model_dump() 
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            # Asumiendo Pydantic v2+, usar model_dump(). Para v1, sería obj_in.dict().
            update_data = obj_in.model_dump(exclude_unset=True) 
        
        for field in update_data:
            if hasattr(db_obj, field): # Verificar si el campo existe en el modelo SQLAlchemy
                setattr(db_obj, field, update_data[field])
        
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: Any) -> ModelType | None:
        obj = db.query(self.model).get(id)
        if obj:
            db.delete(obj)
            db.commit()
        return obj

# Podrías instanciar managers para cada modelo si lo deseas, por ejemplo:
# from .models import Empresa, Sucursal # Asegúrate que los modelos estén definidos
# from datetime import datetime # Necesario para el ejemplo de EmpresaInDB

# class EmpresaBasePydantic(BaseModel): # Renombrado para evitar conflicto con el modelo SQLAlchemy
#     nit: str
#     razon_social: str

# class EmpresaCreatePydantic(EmpresaBasePydantic): # Renombrado
#     pass

# class EmpresaUpdatePydantic(EmpresaBasePydantic): # Renombrado
#     # Aquí podrías hacer algunos campos opcionales si es necesario
#     nit: Optional[str] = None
#     razon_social: Optional[str] = None

# class EmpresaInDBPydantic(EmpresaBasePydantic): # Renombrado
#     id: int
#     creado_en: datetime
#     actualizado_en: datetime

#     class Config:
#         from_attributes = True # Para Pydantic v2. Para v1 es orm_mode = True

# Y luego:
# empresa_manager = CRUDManager[Empresa, EmpresaCreatePydantic, EmpresaUpdatePydantic](Empresa)
