from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base

class Feedbacks(Base):
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    position = Column(String, nullable=True)
    name = Column(String, nullable=False)
    image = Column(String, nullable=True)
    feedback_text = Column(String(length=20), nullable=False)

    
