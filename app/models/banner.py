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
<<<<<<< HEAD
    bg_image = Column(ImageType(storage=FileSystemStorage(path="app/media/banner")), nullable=True)
    phone_num = Column(String(length=20), nullable=False)
=======
    bg_image = Column(ImageType(storage=FileSystemStorage(path="media/banner")), nullable=True)
    phone_num = Column(String(length=20), nullable=False)

#
# class Why_we_us(Base):
#     __tablename__ = 'why_we_us'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     title = Column(String, nullable=False)
#     desc = Column(String, nullable=False)
>>>>>>> 634d1187a51850019666e0e4f130ef69763c4d5f
