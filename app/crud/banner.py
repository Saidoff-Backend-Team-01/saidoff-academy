from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.schemas.banner import BannerListSchema, BannerCreateSchema
from app.models.company import Banner


def get_banners(db: Session):
    return db.query(Banner).all()



def get_why_we_us(db: Session):
    return db.query(Banner).order_by(desc(Banner.id)).limit(3).all()


def get_services(db: Session):
    return db.query(Banner).order_by(desc(Banner.id)).limit(8).all()


def create_banner(db: Session, banner_create: BannerCreateSchema):
    db_banner = Banner(**banner_create.dict())
    db.add(db_banner)
    db.commit()
    db.refresh(db_banner)
    return db_banner