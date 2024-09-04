from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.config.database import Base

class Portfolio(Base):
    __tablename__ = 'portfolio'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=255), nullable=False)
    description = Column(Text, nullable=False)
    button_text = Column(String(length=50), nullable=True)

    categories = relationship("PortfolioCategory", back_populates="portfolio")

class PortfolioCategory(Base):
    __tablename__ = 'portfolio_category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False)
    portfolio_id = Column(Integer, ForeignKey('portfolio.id'), nullable=False)

    portfolio = relationship("Portfolio", back_populates="categories")

    items = relationship("PortfolioItem", back_populates="category")

class PortfolioItem(Base):
    __tablename__ = 'portfolio_item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=255), nullable=False)
    image = Column(String(length=255), nullable=False)
    category_id = Column(Integer, ForeignKey('portfolio_category.id'), nullable=False)

    category = relationship("PortfolioCategory", back_populates="items")
