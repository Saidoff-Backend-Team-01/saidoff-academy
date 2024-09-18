from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

<<<<<<< HEAD
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:sayfullo077@localhost/saidoff_academy"
=======
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://saidadmin:123@localhost/saidb"
>>>>>>> 634d1187a51850019666e0e4f130ef69763c4d5f

SQLALCHEMY_DATABASE_URL_TESTING = "postgresql://postgres:sayfullo077@localhost/saidoff_academy_test"

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