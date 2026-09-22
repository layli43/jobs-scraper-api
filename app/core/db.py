from collections.abc import Generator

from sqlmodel import create_engine, Session

from app.core.config import settings

engine = create_engine(str(settings.DATABASE_URL), pool_pre_ping=True)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


# make sure all SQLModel models are imported (app.models) before initializing DB
# otherwise, SQLModel might fail to initialize relationships properly
# for more details: https://github.com/fastapi/full-stack-fastapi-template/issues/28
