from sqlalchemy.orm import Session

from app.models.custumers import ContactUS
from app.schemas.custumer_schemas import ContactUSModel



def post_contact_us(db: Session, contact: ContactUSModel):
    contact_us = ContactUS(**contact.dict())

    db.add(contact_us)
    db.commit()
    db.refresh(contact_us)

    return contact_us