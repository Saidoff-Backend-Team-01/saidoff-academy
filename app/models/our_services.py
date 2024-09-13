from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base


class OurServices(Base):
    __tablename__ = 'our_services'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=255), nullable=False)
    desc = Column(String, nullable=False)
    image = Column(String, nullable=False)
    slug = Column(String, nullable=False)

    service_infos = relationship("OurServiceInfo", back_populates="service")


class OurServiceInfo(Base):
    __tablename__ = 'our_service_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    service_id = Column(Integer, ForeignKey('our_services.id'), nullable=False)
    additional_info = Column(String, nullable=False)

    service = relationship("OurServices", back_populates="service_infos")
