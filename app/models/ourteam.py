from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
# from fastapi_storages.integrations.sqlalchemy import ImageType
from app.config.database import Base


class Ourteam(Base):
    __tablename__ = 'ourteam'

    id = Column(Integer, primary_key=True, autoincrement=True)
    position = Column(String, nullable=False)
    name = Column(String, nullable=False)
    # image_data = Column(ImageType, nullable=False)

    # image_url = Column(String, nullable=True)
    # image_id = Column(Integer, ForeignKey('images.id'))
    # image = Column(LargeBinary, nullable=True)
    # image = relationship('image', back_populates='ourteam')


