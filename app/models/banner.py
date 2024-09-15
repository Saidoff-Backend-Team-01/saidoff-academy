from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType

from app.config.database import Base


class Banner(Base):
    __tablename__ = 'banner'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    desc = Column(String, nullable=False)
    bg_image = Column(ImageType(storage=FileSystemStorage(path="app/media/banner")), nullable=True)
    phone_num = Column(String(length=20), nullable=False)