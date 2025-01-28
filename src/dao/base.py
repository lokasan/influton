from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession, AsyncConnection

from src.database import connection_and_session


class BaseDAO:
    model = None

    @classmethod
    @connection_and_session
    async def find_by_id(cls, connection: AsyncConnection,
                         session: AsyncSession, model_id: int):
        query = select(cls.model).filter_by(id=model_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    @connection_and_session
    async def find_one_or_none(cls, connection: AsyncConnection,
                               session: AsyncSession, **filter_by):
        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    @connection_and_session
    async def find_all(cls, connection: AsyncConnection, session: AsyncSession,
                       **filter_by):
        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    @connection_and_session
    async def add(cls, connection: AsyncConnection, session: AsyncSession,
                  **kwargs):
        query = insert(cls.model).values(**kwargs)
        await session.execute(query)
        await session.commit()
