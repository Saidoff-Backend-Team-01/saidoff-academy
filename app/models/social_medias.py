from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base

class SocialMedias(Base):
    __tablename__ = 'social_medias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    image = Column(String, nullable=False)
    link = Column(String, nullable=False)

    
