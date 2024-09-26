from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import validates

from app.config.database import Base

class Config(Base):
    __tablename__ = 'config'

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String(length=30), nullable=False)
    email = Column(String(length=100), nullable=False)


    @validates('email')
    def validate_email(self, key, value):
        if not '@gmail.com' in value:
            raise ValueError('Wrong email')
        
        return value