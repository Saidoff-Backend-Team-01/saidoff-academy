from sqlalchemy.orm import Session

from app.models.common import SocialMedia




def get_socialmedia(db: Session):
    return db.query(SocialMedia).all()