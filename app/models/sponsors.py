from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType

from app.config.database import Base

class Sponsors(Base):
    __tablename__ = 'sponsors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    image = Column(ImageType(storage=FileSystemStorage(path='media/sponsors')), nullable=False)
    url = Column(String, nullable=False)


    
