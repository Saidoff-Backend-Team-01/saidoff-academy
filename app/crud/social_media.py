from sqlalchemy.orm import Session

from app.models.social_medias import SocialMedias




def get_socialmedia(db: Session):
    return db.query(SocialMedias).all()