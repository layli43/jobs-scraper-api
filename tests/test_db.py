from sqlmodel import Session, create_engine, text

from app.core.config import settings


def test_db_connection() -> None:
    engine = create_engine(str(settings.DATABASE_URL), pool_pre_ping=True)
    with Session(engine) as session:
        result = session.exec(text("select 1")).first()
    assert result == (1,)
