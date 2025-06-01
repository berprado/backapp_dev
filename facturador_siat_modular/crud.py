from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session, DeclarativeBase

from .database.models import Base # Asumiendo que Base está en models.py

ModelType = TypeVar("ModelType", bound=Any)  # Cambiamos a Any para evitar el error
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        :param model: A SQLAlchemy model class
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
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
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True) # Pydantic V2
            # update_data = obj_in.dict(exclude_unset=True) # Pydantic V1
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).filter(self.model.id == id).first()
        if obj is None:
            raise ValueError(f"Object with id {id} not found")
        db.delete(obj)
        db.commit()
        return obj

# Importaciones específicas para Cliente
from .database.models import Cliente
from .schemas.cliente_schemas import ClienteCreate, ClienteUpdate

class CRUDCliente(CRUDBase[Cliente, ClienteCreate, ClienteUpdate]):
    def __init__(self, model: Type[Cliente]):
        super().__init__(model)

    # Aquí puedes añadir métodos específicos para Cliente si son necesarios.
    # Por ejemplo, buscar cliente por nit, etc.
    # def get_by_nit(self, db: Session, *, nit: str) -> Optional[Cliente]:
    #     return db.query(self.model).filter(self.model.nit == nit).first()

# Instancia del CRUD para Cliente
crud_cliente = CRUDCliente(Cliente)

# Importaciones específicas para PuntoVenta
from .database.models import PuntoVenta
from .schemas.punto_venta_schemas import PuntoVentaCreate, PuntoVentaUpdate

class CRUDPuntoVenta(CRUDBase[PuntoVenta, PuntoVentaCreate, PuntoVentaUpdate]):
    def __init__(self, model: Type[PuntoVenta]):
        super().__init__(model)

    # Aquí puedes añadir métodos específicos para PuntoVenta si son necesarios.

# Instancia del CRUD para PuntoVenta
crud_punto_venta = CRUDPuntoVenta(PuntoVenta)

# Importaciones específicas para Sucursal
from .database.models import Sucursal
from .schemas.sucursal_schemas import SucursalCreate, SucursalUpdate

class CRUDSucursal(CRUDBase[Sucursal, SucursalCreate, SucursalUpdate]):
    def __init__(self, model: Type[Sucursal]):
        super().__init__(model)

    # Aquí puedes añadir métodos específicos para Sucursal si son necesarios.

# Instancia del CRUD para Sucursal
crud_sucursal = CRUDSucursal(Sucursal)

# Importaciones específicas para Cufd
from .database.models import Cufd
from .schemas.cufd_schemas import CufdCreate, CufdUpdate

class CRUDCufd(CRUDBase[Cufd, CufdCreate, CufdUpdate]):
    def __init__(self, model: Type[Cufd]):
        super().__init__(model)

    # Aquí puedes añadir métodos específicos para Cufd si son necesarios.
    # Por ejemplo, obtener el CUFD vigente para un punto de venta y sucursal.
    # def get_active_cufd(self, db: Session, *, punto_venta_id: int, sucursal_id: int) -> Optional[Cufd]:
    #     from sqlalchemy import and_
    #     from datetime import datetime
    #     return (
    #         db.query(self.model)
    #         .filter(
    #             and_(
    #                 self.model.punto_venta_id == punto_venta_id,
    #                 self.model.sucursal_id == sucursal_id,
    #                 self.model.fecha_vigencia >= datetime.utcnow(),
    #                 self.model.activo == True # Asumiendo que tienes un campo 'activo'
    #             )
    #         )
    #         .order_by(self.model.fecha_vigencia.desc())
    #         .first()
    #     )

# Instancia del CRUD para Cufd
crud_cufd = CRUDCufd(Cufd)

# Importaciones específicas para Factura
from .database.models import Factura
from .schemas.factura_schemas import FacturaCreate, FacturaUpdate

class CRUDFactura(CRUDBase[Factura, FacturaCreate, FacturaUpdate]):
    def __init__(self, model: Type[Factura]):
        super().__init__(model)

    # Aquí puedes añadir métodos específicos para Factura si son necesarios.
    # Por ejemplo, buscar facturas por cliente, por rango de fechas, etc.
    # def get_by_cliente_id(self, db: Session, *, cliente_id: int, skip: int = 0, limit: int = 100) -> List[Factura]:
    #     return db.query(self.model).filter(self.model.cliente_id == cliente_id).offset(skip).limit(limit).all()

# Instancia del CRUD para Factura
crud_factura = CRUDFactura(Factura)

# Importaciones específicas para DetalleFactura
from .database.models import DetalleFactura
from .schemas.detalle_factura_schemas import DetalleFacturaCreate, DetalleFacturaUpdate

class CRUDDetalleFactura(CRUDBase[DetalleFactura, DetalleFacturaCreate, DetalleFacturaUpdate]):
    def __init__(self, model: Type[DetalleFactura]):
        super().__init__(model)

    # Aquí puedes añadir métodos específicos para DetalleFactura si son necesarios.
    # Por ejemplo, obtener todos los detalles de una factura específica.
    # def get_by_factura_id(self, db: Session, *, factura_id: int) -> List[DetalleFactura]:
    #     return db.query(self.model).filter(self.model.factura_id == factura_id).all()

# Instancia del CRUD para DetalleFactura
crud_detalle_factura = CRUDDetalleFactura(DetalleFactura)

# Importaciones específicas para EventoContingencia
from .database.models import EventoContingencia
from .schemas.evento_contingencia_schemas import EventoContingenciaCreate, EventoContingenciaUpdate

class CRUDEventoContingencia(CRUDBase[EventoContingencia, EventoContingenciaCreate, EventoContingenciaUpdate]):
    def __init__(self, model: Type[EventoContingencia]):
        super().__init__(model)

    # Aquí puedes añadir métodos específicos para EventoContingencia si son necesarios.
    # Por ejemplo, buscar eventos de contingencia activos para un punto de venta.
    # def get_active_contingency_by_pv(self, db: Session, *, punto_venta_id: int) -> List[EventoContingencia]:
    #     from sqlalchemy import and_
    #     return (
    #         db.query(self.model)
    #         .filter(
    #             and_(
    #                 self.model.punto_venta_id == punto_venta_id,
    #                 self.model.fecha_hora_fin_evento == None  # Asumiendo que None significa activo
    #             )
    #         )
    #         .all()
    #     )

# Instancia del CRUD para EventoContingencia
crud_evento_contingencia = CRUDEventoContingencia(EventoContingencia)

# Importaciones específicas para TipoPuntoVentaSiat
from .database.models import TipoPuntoVentaSiat
from .schemas.tipo_punto_venta_siat_schemas import TipoPuntoVentaSiatCreate, TipoPuntoVentaSiatUpdate

class CRUDTipoPuntoVentaSiat(CRUDBase[TipoPuntoVentaSiat, TipoPuntoVentaSiatCreate, TipoPuntoVentaSiatUpdate]):
    def __init__(self, model: Type[TipoPuntoVentaSiat]):
        super().__init__(model)

    # Aquí puedes añadir métodos específicos para TipoPuntoVentaSiat si son necesarios.

# Instancia del CRUD para TipoPuntoVentaSiat
crud_tipo_punto_venta_siat = CRUDTipoPuntoVentaSiat(TipoPuntoVentaSiat)

# Importaciones específicas para TipoHabitacionSiat
from .database.models import TipoHabitacionSiat
from .schemas.tipo_habitacion_siat_schemas import TipoHabitacionSiatCreate, TipoHabitacionSiatUpdate

class CRUDTipoHabitacionSiat(CRUDBase[TipoHabitacionSiat, TipoHabitacionSiatCreate, TipoHabitacionSiatUpdate]):
    def __init__(self, model: Type[TipoHabitacionSiat]):
        super().__init__(model)

    # Aquí puedes añadir métodos específicos para TipoHabitacionSiat si son necesarios.

# Instancia del CRUD para TipoHabitacionSiat
crud_tipo_habitacion_siat = CRUDTipoHabitacionSiat(TipoHabitacionSiat)

# Importaciones específicas para LeyendaFacturaSiat
from .database.models import LeyendaFacturaSiat
from .schemas.leyenda_factura_siat_schemas import LeyendaFacturaSiatCreate, LeyendaFacturaSiatUpdate

class CRUDLeyendaFacturaSiat(CRUDBase[LeyendaFacturaSiat, LeyendaFacturaSiatCreate, LeyendaFacturaSiatUpdate]):
    def __init__(self, model: Type[LeyendaFacturaSiat]):
        super().__init__(model)

    # Aquí puedes añadir métodos específicos para LeyendaFacturaSiat si son necesarios.

# Instancia del CRUD para LeyendaFacturaSiat
crud_leyenda_factura_siat = CRUDLeyendaFacturaSiat(LeyendaFacturaSiat)

# Importaciones específicas para ProductoServicioSiat
from .database.models import ProductoServicioSiat
from .schemas.producto_servicio_siat_schemas import ProductoServicioSiatCreate, ProductoServicioSiatUpdate

class CRUDProductoServicioSiat(CRUDBase[ProductoServicioSiat, ProductoServicioSiatCreate, ProductoServicioSiatUpdate]):
    def __init__(self, model: Type[ProductoServicioSiat]):
        super().__init__(model)

    # Aquí puedes añadir métodos específicos para ProductoServicioSiat si son necesarios.

# Instancia del CRUD para ProductoServicioSiat
crud_producto_servicio_siat = CRUDProductoServicioSiat(ProductoServicioSiat)

# Importaciones específicas para TipoEventoSignificativoSiat
from .database.models import TipoEventoSignificativoSiat
from .schemas.tipo_evento_significativo_siat_schemas import TipoEventoSignificativoSiatCreate, TipoEventoSignificativoSiatUpdate

class CRUDTipoEventoSignificativoSiat(CRUDBase[TipoEventoSignificativoSiat, TipoEventoSignificativoSiatCreate, TipoEventoSignificativoSiatUpdate]):
    def __init__(self, model: Type[TipoEventoSignificativoSiat]):
        super().__init__(model)

    # Aquí puedes añadir métodos específicos para TipoEventoSignificativoSiat si son necesarios.

# Instancia del CRUD para TipoEventoSignificativoSiat
crud_tipo_evento_significativo_siat = CRUDTipoEventoSignificativoSiat(TipoEventoSignificativoSiat)

# Importaciones específicas para PaisOrigenSiat
from .database.models import PaisOrigenSiat
from .schemas.pais_origen_siat_schemas import PaisOrigenSiatCreate, PaisOrigenSiatUpdate

class CRUDPaisOrigenSiat(CRUDBase[PaisOrigenSiat, PaisOrigenSiatCreate, PaisOrigenSiatUpdate]):
    def __init__(self, model: Type[PaisOrigenSiat]):
        super().__init__(model)

    # Aquí puedes añadir métodos específicos para PaisOrigenSiat si son necesarios.

# Instancia del CRUD para PaisOrigenSiat
crud_pais_origen_siat = CRUDPaisOrigenSiat(PaisOrigenSiat)

# Importaciones específicas para ActividadDocumentoSectorSiat
from .database.models import ActividadDocumentoSectorSiat
from .schemas.actividad_documento_sector_siat_schemas import ActividadDocumentoSectorSiatCreate, ActividadDocumentoSectorSiatUpdate

class CRUDActividadDocumentoSectorSiat(CRUDBase[ActividadDocumentoSectorSiat, ActividadDocumentoSectorSiatCreate, ActividadDocumentoSectorSiatUpdate]):
    def __init__(self, model: Type[ActividadDocumentoSectorSiat]):
        super().__init__(model)

    # Aquí puedes añadir métodos específicos para ActividadDocumentoSectorSiat si son necesarios.

# Instancia del CRUD para ActividadDocumentoSectorSiat
crud_actividad_documento_sector_siat = CRUDActividadDocumentoSectorSiat(ActividadDocumentoSectorSiat)

# Importaciones específicas para MensajeServicioSiat
from .database.models import MensajeServicioSiat
from .schemas.mensaje_servicio_siat_schemas import MensajeServicioSiatCreate, MensajeServicioSiatUpdate

class CRUDMensajeServicioSiat(CRUDBase[MensajeServicioSiat, MensajeServicioSiatCreate, MensajeServicioSiatUpdate]):
    def __init__(self, model: Type[MensajeServicioSiat]):
        super().__init__(model)

    # Aquí puedes añadir métodos específicos para MensajeServicioSiat si son necesarios.

# Instancia del CRUD para MensajeServicioSiat
crud_mensaje_servicio_siat = CRUDMensajeServicioSiat(MensajeServicioSiat)

# Importaciones específicas para ActividadSiat
from .database.models import ActividadSiat
from .schemas.actividad_siat_schemas import ActividadSiatCreate, ActividadSiatUpdate

class CRUDActividadSiat(CRUDBase[ActividadSiat, ActividadSiatCreate, ActividadSiatUpdate]):
    def __init__(self, model: Type[ActividadSiat]):
        super().__init__(model)

    # Aquí puedes añadir métodos específicos para ActividadSiat si son necesarios.

# Instancia del CRUD para ActividadSiat
crud_actividad_siat = CRUDActividadSiat(ActividadSiat)
