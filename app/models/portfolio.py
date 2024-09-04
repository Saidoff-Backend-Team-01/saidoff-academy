from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType

from app.config.database import Base


class ResultCategory(Base):
    __tablename__ = 'result_category'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=100), unique=True)

    category_results = relationship('OurResult', back_populates='results')





class OurResult(Base):
    __tablename__ = 'our_result'

    id = Column(Integer, primary_key=True, index=True)
    image = Column(ImageType(FileSystemStorage(path='static/our_result')))
    category = Column(Integer, ForeignKey('result_category.id'), nullable=False)



class OurWork(Base):
    __tablename__ = 'our_work'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100), unique=True)
    desc = Column(Text)
    image = Column(ImageType(FileSystemStorage(path='static/our_work')))

    our_work_details = relationship('OurWorkDetail', back_populates='details')


class OurWorkDetail(Base):
    __tablename__ = 'our_work_detail'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100), unique=True)
    desc = Column(Text)
    image = Column(ImageType(FileSystemStorage(path='static/our_work_detail')))
    our_work = Column(Integer, ForeignKey('our_work.id'), nullable=False)