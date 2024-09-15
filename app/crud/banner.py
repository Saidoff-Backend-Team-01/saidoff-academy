from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.schemas.banner import BannerListSchema, BannerCreateSchema
from app.models.banner import Banner
from app.models.why_we_us import WhyWeUs


# def get_banners(db: Session):
#     return db.query(Banner).filter(Banner.id).first()


def get_banners(db: Session):
    return db.query(Banner).first()


def get_why_we_us(db: Session):
    return db.query(WhyWeUs).order_by(desc(WhyWeUs.id)).limit(3).all()


def create_banner(db: Session, banner_create: BannerCreateSchema):
    db_banner = Banner(**banner_create.dict())
    db.add(db_banner)
    db.commit()
    db.refresh(db_banner)
    return db_banner



def get_portfolio_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PortfolioCategory).offset(skip).limit(limit).all()

def get_portfolio_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PortfolioItem).offset(skip).limit(limit).all()

def get_portfolio_items_by_category(db: Session, category_id: int):
    return db.query(models.PortfolioItem).filter(models.PortfolioItem.category_id == category_id).all()

def get_customer_feedbacks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Feedbacks).offset(skip).limit(limit).all()



