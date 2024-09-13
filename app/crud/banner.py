from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.schemas.banner import BannerListSchema, BannerCreateSchema
from app.models.banner import Banner, Why_we_us


def get_banners(db: Session):
    return db.query(Banner).all()



def get_why_we_us(db: Session):
    return db.query(Why_we_us).order_by(desc(Why_we_us.id)).limit(3).all()



def create_banner(db: Session, banner_create: BannerCreateSchema):
    db_banner = Banner(**banner_create.dict())
    db.add(db_banner)
    db.commit()
    db.refresh(db_banner)
    return db_banner



# def get_portfolio_categories(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.PortfolioCategory).offset(skip).limit(limit).all()
#
# def get_portfolio_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.PortfolioItem).offset(skip).limit(limit).all()
#
# def get_portfolio_items_by_category(db: Session, category_id: int):
#     return db.query(models.PortfolioItem).filter(models.PortfolioItem.category_id == category_id).all()
#
# def get_customer_feedbacks(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Feedbacks).offset(skip).limit(limit).all()



