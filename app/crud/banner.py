from sqlalchemy.orm import Session


from app.schemas.banner import BannerListSchema, BannerCreateSchema
from app.models.banner import Banner
from app.models.why_we_us import WhyWeUs

from app.schemas.banner import BannerCreateSchema
from app.models.banner import Banner
from app.models.customer_feedback import Feedbacks

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



def get_customer_feedbacks(db: Session):
    return db.query(Feedbacks).all()



