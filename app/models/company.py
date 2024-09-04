from sqlalchemy import Column, String, Integer, Text, CheckConstraint
from sqlalchemy.orm import validates
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType

from app.config.database import Base


class WhyWe(Base):
    __tablename__ = 'why_we'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100), unique=True)
    desc = Column(Text)


class Sponsor(Base):
    __tablename__ = 'sponsor' 

    id = Column(Integer, primary_key=True, index=True)
    image = Column(ImageType(FileSystemStorage(path='static/sponsor')))
    url = Column(Text)


    @validates('url')
    def validate_url(self, key, value):
        if not 'http' in value and not 'https' in value:
            raise ValueError('Incorrect url')
        
        return value
    

class OurTeamMember(Base):
    __tablename__ = 'our_team_member'

    id = Column(Integer, primary_key=True, index=True)
    job = Column(String(length=100))
    full_name = Column(String(length=200))
    experience = Column(Integer)
    image = Column(ImageType(FileSystemStorage(path='static/our_team_member')))


    @validates('experience')
    def validate_experience(self, key, value):
        if value < 1:
            raise ValueError('Experience must be minimum one year')
        return value

class FAQ(Base):
    __tablename__ = 'faq'

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text)
    answer = Column(Text)
    order = Column(Integer)
    type = Column(String(length=50), CheckConstraint("type IN ('General', 'Company')"))

    @validates('order')
    def validate_order(self, key, value):
        if value < 1:
            raise ValueError('Order must be minimum one')
        return value