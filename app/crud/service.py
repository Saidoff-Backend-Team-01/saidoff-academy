from sqlalchemy import desc
from sqlalchemy.orm import Session
from .services import get_services
from app.schemas.banner import BannerListSchema, BannerCreateSchema
from app.models.our_services import OurServices


def get_service(db: Session):
    return db.query(OurServices).order_by(desc(OurServices.id)).limit(8).all()
