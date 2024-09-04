from sqlalchemy import Column, Text, String, Integer

from app.config.database import Base


class ContactUS(Base):
    __tablename__ = 'contactus'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50))
    phone = Column(String(length=15))
    

class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=70))
    job = Column(String(length=70))
    desc = Column(Text)
    image = Column(Text)