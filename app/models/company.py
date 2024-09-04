from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base


class Banner(Base):
    __tablename__ = 'banner'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    desc = Column(String, nullable=False)

    
