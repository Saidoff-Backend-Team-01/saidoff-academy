from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base


class WhyWeUs(Base):
    __tablename__ = 'why_we_us'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    desc = Column(String, nullable=False)
    bg_image = Column(String, nullable=False)

    class Meta:
        extend_existing = True
