import os
import sys
from logging.config import fileConfig

from sqlalchemy import create_engine, pool # Usar create_engine directamente

from alembic import context

# Añadir el directorio raíz del proyecto al sys.path
# Esto permite que Alembic encuentre los módulos de la aplicación, como config.py y models.py
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

# Importar la configuración de la aplicación y la Base de los modelos
# Asegúrate de que la ruta de importación sea correcta según la estructura de tu proyecto
from facturador_siat_modular.config import config as app_config  # Renombrado para evitar conflicto de nombres
from facturador_siat_modular.database.models import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired: # my_important_option = config.get_main_option("my_important_option")
# ... etc.

def get_url():
    return app_config.DATABASE_URL # Usar la URL de la configuración de la aplicación

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    # Modificado para usar create_engine directamente con la URL de la app_config
    db_url = get_url()
    connectable = create_engine(db_url, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
