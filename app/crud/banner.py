from sqlalchemy.orm import Session


from app.schemas.banner import BannerCreateSchema
from app.models.banner import Banner
from app.models.customer_feedback import Feedbacks

def get_banners(db: Session):
    return db.query(Banner).all()




def create_banner(db: Session, banner_create: BannerCreateSchema):
    db_banner = Banner(**banner_create.dict())
    db.add(db_banner)
    db.commit()
    db.refresh(db_banner)
    return db_banner



def get_customer_feedbacks(db: Session):
    return db.query(Feedbacks).all()



