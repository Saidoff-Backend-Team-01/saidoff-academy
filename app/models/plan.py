from sqlalchemy import Column, String, Integer, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship, validates

from app.config.database import Base


class Plan(Base):
    __tablename__ = 'plan'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, unique=True)
    price = Column(Integer, nullable=False)
    is_popular = Column(Boolean, default=False)
    desc = Column(Text)

    features = relationship('Feature', back_populates='plans')


    @validates('price')
    def validate_price(self, key, value):
        if value < 1:
            raise ValueError('Price have to be minimum 1')
        
        return value
    
    def __str__(self):
        return self.name
    



class Feature(Base):
    __tablename__ = 'feature'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=250), nullable=False)
    plan_id = Column(Integer, ForeignKey('plan.id'), nullable=False)

    plans = relationship('Plan', back_populates='features')


    def __str__(self):
        return self.name
