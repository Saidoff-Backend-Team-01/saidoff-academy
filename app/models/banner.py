from fastapi_storages import FileSystemStorage
from sqlalchemy import Column, Integer, String, Text, Enum

import enum

from app.config.database import Base


class PageType(enum.Enum):
    MAIN = 'homepage'
    ABOUT = 'aboutus'
    PORTFOLIO = 'portfolio'

class Banner(Base):
    __tablename__ = 'banner'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    desc = Column(Text, nullable=False)
    page_type = Column(Enum(PageType), nullable=False)
