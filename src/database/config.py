from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.config import settings


class Base(DeclarativeBase):
    pass


async_engine = create_async_engine(settings.db.url)
async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_session():
    async with async_session_factory() as session:
        yield session
