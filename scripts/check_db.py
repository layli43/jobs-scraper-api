from sqlmodel import Session, create_engine, text

from app.core.config import settings


def main() -> None:
    engine = create_engine(str(settings.DATABASE_URL), pool_pre_ping=True)
    with Session(engine) as session:
        version = session.exec(text("SELECT version()")).first()
        print(f"Connected OK: {version[0]}")


if __name__ == "__main__":
    main()
