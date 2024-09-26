from sqlalchemy import Column, Integer, String
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType

from app.config.database import Base


class OurTeam(Base):
    __tablename__ = 'our_team'

    id = Column(Integer, primary_key=True, autoincrement=True)
    position = Column(String, nullable=False)
    name = Column(String, nullable=False)
    image = Column(ImageType(storage=FileSystemStorage(path='media/our_team')), nullable=False)
    experience = Column(String, nullable=False)

    
