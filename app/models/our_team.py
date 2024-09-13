from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.config.database import Base


class OurTeam(Base):
    __tablename__ = 'our_team'

    id = Column(Integer, primary_key=True, autoincrement=True)
    position = Column(String, nullable=False)
    name = Column(String, nullable=False)
    image = Column(String, nullable=False)
    experience = Column(String, nullable=False)

    
