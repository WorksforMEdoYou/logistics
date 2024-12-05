
import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.engine import Connection
from alembic import context
from app.models import Base  # Ensure this import is correct for the project structure 

# Load environment variables
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://avnadmin:AVNS_N-gHgacEmIMkzjnFIkN@pg-ce9484b-dualipa7102002-7bb9.i.aivencloud.com:14761/defaultdb"
)

# Create an async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Alembic Configurations
config = context.config
target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection):
    """Run migrations using the provided connection."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,  # Optional: compare column types
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in 'online' mode."""
    async with engine.connect() as async_connection:
        # Use a synchronous wrapper for async connections
        await async_connection.run_sync(do_run_migrations)


if context.is_offline_mode():
    run_migrations_offline()
else:
    import asyncio
    asyncio.run(run_migrations_online())