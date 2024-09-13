from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum

from app.config.database import Base


class FaqType(Enum):
    GENERAL = "general"
    COMPANY = "company"


class Faq(Base):
    __tablename__ = 'faq'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    faq_type = Column(Enum(FaqType), nullable=False)




