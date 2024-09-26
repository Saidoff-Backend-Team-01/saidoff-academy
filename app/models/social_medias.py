from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType

from app.config.database import Base

class SocialMedias(Base):
    __tablename__ = 'social_medias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    image = Column(ImageType(storage=FileSystemStorage(path='media/socialmedia')), nullable=False)
    link = Column(String, nullable=False)

    
