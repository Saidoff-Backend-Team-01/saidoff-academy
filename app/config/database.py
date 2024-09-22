from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:shahzod0604@localhost/SaidoffGroup"

SQLALCHEMY_DATABASE_URL_TESTING = "postgresql://postgres:shahzod0604@localhost/SaidoffAcademy"

if os.environ.get('ENVIRONMENT') == "testing":
     engine = create_engine(
     SQLALCHEMY_DATABASE_URL_TESTING,
    )
else:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
