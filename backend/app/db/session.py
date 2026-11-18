from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from app.core.config import setting


# the engine manages the database connection

engine = create_async_engine(setting.database_url)

sessionlocal = async_sessionmaker(engine,expire_on_commit = False)

async def get_db():
    async with sessionlocal as session:
        yield session