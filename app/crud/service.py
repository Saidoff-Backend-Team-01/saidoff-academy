from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.schemas.banner import BannerListSchema, BannerCreateSchema
from app.models.services import Service


def get_services(db: Session):
    return db.query(Service).order_by(desc(Service.id)).limit(8).all()