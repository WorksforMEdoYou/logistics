# app/database.py
import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://avnadmin:AVNS_N-gHgacEmIMkzjnFIkN@pg-ce9484b-dualipa7102002-7bb9.i.aivencloud.com:14761/defaultdb")

# Create an async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a sessionmaker for async sessions
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session