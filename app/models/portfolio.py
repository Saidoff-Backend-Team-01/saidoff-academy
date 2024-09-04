from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base


class ResultCategory(Base):
    __tablename__ = 'result_category'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=100), unique=True)

    category_results = relationship('OurResult', back_populates='results')





class OurResult(Base):
    __tablename__ = 'our_result'

    id = Column(Integer, primary_key=True, index=True)
    image = Column(Text)
    category = Column(Integer, ForeignKey('result_category.id'), nullable=False)



class OurWork(Base):
    __tablename__ = 'our_work'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100), unique=True)
    desc = Column(Text)
    image = Column(Text)

    our_work_details = relationship('OurWorkDetail', back_populates='details')


class OurWorkDetail(Base):
    __tablename__ = 'our_work_detail'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100), unique=True)
    desc = Column(Text)
    image = Column(Text)
    our_work = Column(Integer, ForeignKey('our_work.id'), nullable=False)