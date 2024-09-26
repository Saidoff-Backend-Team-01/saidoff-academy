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
    bg_image = Column(ImageType(storage=FileSystemStorage(path="app/media/banner")), nullable=True)
    phone_num = Column(String(length=20), nullable=False)
    desc = Column(Text, nullable=False)
    page_type = Column(Enum(PageType), nullable=False)
