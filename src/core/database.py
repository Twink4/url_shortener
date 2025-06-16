from fastapi import Depends
from typing import Annotated
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)

from sqlalchemy.orm import DeclarativeBase

from .config import settings

engine: AsyncEngine = create_async_engine(
    settings.db_config.async_database_url,
    echo=True
)

async_session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class Base(DeclarativeBase):
    ...


async def get_async_session() -> AsyncGenerator:
    async with async_session_maker() as session:
        yield session

DependsSession = Annotated[AsyncSession, Depends(get_async_session)]