from sqlalchemy import Column, Integer, String
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType

from app.config.database import Base


class WhyWeUs(Base):
    __tablename__ = 'why_we_us'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    desc = Column(String, nullable=False)
    bg_image = Column(ImageType(storage=FileSystemStorage(path='media/why_we')), nullable=False)

    class Meta:
        extend_existing = True
