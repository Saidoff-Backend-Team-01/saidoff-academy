from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base

class Sponsors(Base):
    __tablename__ = 'sponsors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    image = Column(String, nullable=False)
    url = Column(String, nullable=False)


    
