from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base

class ContactWithUs(Base):
    __tablename__ = 'contact_with_us'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)
    phone_number = Column(String, nullable=False)

    

