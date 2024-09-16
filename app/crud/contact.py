from sqlalchemy.orm import Session

from app.models.contact_with_us import ContactWithUs
from app.schemas.contact import ContactUSModel



def post_contact_us(db: Session, contact: ContactUSModel):
    contact_us = ContactWithUs(**contact.dict())

    db.add(contact_us)
    db.commit()
    db.refresh(contact_us)

    return contact_us