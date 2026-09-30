from app.config import DATABASE_URL
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker 
from sqlalchemy.orm import DeclarativeBase

async_engine = create_async_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=10
)

SessionLocal = async_sessionmaker(async_engine,expire_on_commit=False)

class Base(DeclarativeBase):
    pass