from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.exc import SQLAlchemyError

from config import settings


async def create_async_engine_and_session():
    """Creates an asynchronous SQLAlchemy engine and session factory.

    This function establishes a connection to the SQLite database specified
    by the `DATABASE_URL` and
    creates an asynchronous session factory that can be used to create
    sessions for interacting with the database.

    :return: A tuple containing the created engine and session factory objects.
    """
    engine = create_async_engine(settings.DATABASE_URL, echo=False)
    async_session = sessionmaker(bind=engine, class_=AsyncSession,
                                 expire_on_commit=False, autoflush=False)

    return engine, async_session


def connection_and_session(func):
    """Decorator for managing database connections and sessions for asynchronous functions.

    This decorator simplifies database interactions by handling
    the creation of the engine and session,
    managing transactions, and ensuring proper cleanup when the
    decorated function exits, even in case of exceptions.

    :param func: The asynchronous function to be decorated.

    :return: async function: The decorated asynchronous function with
    automatic connection and session management.
    """

    async def wrapper(cls, *args, **kwargs):
        try:
            if not hasattr(cls, 'engine') or not hasattr(cls,
                                                         'async_session'):
                cls.engine, cls.async_session = await create_async_engine_and_session()
            async with cls.engine.begin() as connection:
                async with cls.async_session() as session:
                    return await func(cls, connection, session, *args,
                                      **kwargs)

        except SQLAlchemyError as e:
            print(f'SQLAlchemy Error: {e}')

    return wrapper


class Base(DeclarativeBase):
    pass
