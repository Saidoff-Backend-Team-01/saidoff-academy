from sqlalchemy.orm import Session
from typing import Optional

from app.models.faq import Faq


# def get_faq(db: Session):
#     return db.query(Faq).all()
def get_faq(db: Session, faq_type: Optional[str] = None):
    query = db.query(Faq)

    if faq_type:
        query = query.filter(Faq.faq_type == faq_type)

    return query.all()
