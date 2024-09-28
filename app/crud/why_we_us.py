from sqlalchemy.orm import Session

from app.models.why_we_us import WhyWeUs


def whywe_get(db: Session):
    return db.query(WhyWeUs).all()