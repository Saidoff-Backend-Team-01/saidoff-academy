from sqlalchemy import Column, Text, String, Integer

from app.config.database import Base

from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType


storage = FileSystemStorage(path="static/feedback")


class ContactUS(Base):
    __tablename__ = 'contactus'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50))
    phone = Column(String(length=15))
    

class Feedback(Base):
    __tablename__ = 'feedback'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=70))
    job = Column(String(length=70))
    desc = Column(Text)
    image = Column(ImageType(storage=storage))