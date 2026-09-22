from sqlmodel import create_engine
import logging

from app.core.config import settings

logger = logging.getLogger(__name__)

DATABASE_URL = settings.DATABASE_URL

if DATABASE_URL:
    engine = create_engine(str(settings.DATABASE_URL), pool_pre_ping=True)
else:
    logger.warning("No DATABASE_URL configured, can't connect to database")
    engine = None


# make sure all SQLModel models are imported (app.models) before initializing DB
# otherwise, SQLModel might fail to initialize relationships properly
# for more details: https://github.com/fastapi/full-stack-fastapi-template/issues/28
