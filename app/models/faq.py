import enum
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import validates
from app.config.database import Base


class FaqType(enum.Enum):
    GENERAL = "general"
    COMPANY = "company"


class Faq(Base):
    __tablename__ = 'faq'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    order = Column(Integer, nullable=False)
    faq_type = Column(Enum(FaqType), nullable=False)


    @validates('order')
    def validate_order(self, key, value):
        if value < 1:
            raise ValueError('Oreder have to be minimum 1')
        
        return value

