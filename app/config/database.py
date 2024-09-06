from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config.settings import base_settings

# print("Db passord:", base_settings.DB_PASSWORD)
# print("Db Name:", base_settings.DB_NAME)


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:shahzod0604@localhost/SaidoffGroup"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
