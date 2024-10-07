from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

    translations = relationship("ItemTranslation", back_populates="item")


class ItemTranslation(Base):
    __tablename__ = "item_translations"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    language_code = Column(String(2), index=True)
    translated_name = Column(String, index=True)
    translated_description = Column(String)

    item = relationship("Item", back_populates="translations")
