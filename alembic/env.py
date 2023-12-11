from logging.config import fileConfig
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import pool
from alembic import context

import os
import sys

# Agrega la ruta al directorio de modelos a sys.path
sys.path.append(os.path.join(os.getcwd(), 'applications', 'EscolarSystem', 'models'))

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)
# Combina las metadata de todos los modelos
from sqlalchemy import MetaData

target_metadata = MetaData()

# Importa tus modelos y agrega sus tablas a target_metadata
from student_model import Base as StudentBase
from salon_model import Base as SalonBase
from subject_model import Base as SubjectBase
from attendance_model import Base as AttendanceBase

target_metadata = target_metadata.merge(StudentBase.metadata)
target_metadata = target_metadata.merge(SalonBase.metadata)
target_metadata = target_metadata.merge(SubjectBase.metadata)
target_metadata = target_metadata.merge(AttendanceBase.metadata)

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = create_engine(config.get_main_option("sqlalchemy.url"))

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# ...

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
