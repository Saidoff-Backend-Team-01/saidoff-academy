from sqlalchemy import Column, Integer, String, Text
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType
from sqlalchemy.orm import validates

from app.config.database import Base

storage = FileSystemStorage(path="static/banner")

class Banner(Base):
    __tablename__ = 'banner'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100), nullable=False)
    desc = Column(Text, nullable=False)
    phone = Column(String(length=15))
    image = Column(ImageType(storage=storage))
    email = Column(String(length=150))


    @validates('email')
    def validate_facebook_url(self, key, value):
        if not '@gmail.com' in value:
            raise ValueError('Incorrect email')
        
        return value


    
class SocialMedia(Base):
    __tablename__ = 'socila_media'

    id = Column(Integer, primary_key=True, index=True)
    facebook_url = Column(Text)
    twitter_url = Column(Text)
    vimeo_url = Column(Text)
    youtube_url = Column(Text)


    @validates('facebook_url')
    def validate_facebook_url(self, key, value):
        if not 'http' in value and not 'https' in value:
            raise ValueError('Incorrect url')
        
        return value
        

    @validates('twitter_url')
    def validate_twitter_url(self, key, value):
        if not 'http' in value and not 'https' in value:
            raise ValueError('Incorrect url')
        
        return value
        

    @validates('vimeo_url')
    def validate_vimeo_url(self, key, value):
        if not 'http' in value and not 'https' in value:
            raise ValueError('Incorrect url')
        
        return value
        

    @validates('youtube_url')
    def validate_youtube_url(self, key, value):
        if not 'http' in value and not 'https' in value:
            raise ValueError('Incorrect url')
        
        return value