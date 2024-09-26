from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType

from app.config.database import Base


tag_and_portfolio = Table(
    'tag_and_portfolio', Base.metadata,
    Column('tag_id', Integer, ForeignKey('portfolio_tag.id'), primary_key=True),
    Column('portfolio_id', Integer, ForeignKey('portfolio_item.id'), primary_key=True),

)

class PortfolioTag(Base):
    __tablename__ = 'portfolio_tag'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, unique=True)

    item = relationship("PortfolioItem", secondary=tag_and_portfolio, back_populates="tags")


    def __str__(self):
        return self.name


    

class PortfolioCategory(Base):
    __tablename__ = 'portfolio_category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False)

    items = relationship("PortfolioItem", back_populates="category")


    def __str__(self):
        return self.name




class PortfolioItem(Base):
    __tablename__ = 'portfolio_item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=255), nullable=False)
    image = Column(ImageType(storage=FileSystemStorage(path='media/portfolio')), nullable=False)
    category_id = Column(Integer, ForeignKey('portfolio_category.id'), nullable=False)

    category = relationship("PortfolioCategory", back_populates="items")
    tags = relationship("PortfolioTag", secondary=tag_and_portfolio, back_populates="item")

    def __str__(self):
        return self.title

