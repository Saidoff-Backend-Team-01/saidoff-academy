from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from slugify import slugify
from app.config.database import Base


class Services(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    desc = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    # image

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title)



