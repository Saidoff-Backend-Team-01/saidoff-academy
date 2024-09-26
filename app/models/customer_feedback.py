from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType

from app.config.database import Base

class Feedbacks(Base):
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    position = Column(String, nullable=True)
    name = Column(String, nullable=False)
    image = Column(ImageType(storage=FileSystemStorage(path='media/feedback')))
    feedback_text = Column(String(length=20), nullable=False)

    
