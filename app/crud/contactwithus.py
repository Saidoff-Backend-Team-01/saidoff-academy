from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from sqlalchemy.exc import IntegrityError

from app.models.contact_with_us import ContactWithUs
from app.schemas.contactwithus import ContactWithUsSchema
from app.models.our_services import OurServices


def create_contact(db: Session, contact: ContactWithUsSchema):
    service = db.query(OurServices).filter(OurServices.id == contact.service_type).first()

    if not service:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid service_type"
        )


    db_contact = ContactWithUs(
        name=contact.name,
        phone_number=contact.phone_number,
        msg=contact.msg,
        service_type=contact.service_type  
    )

    try:
        db.add(db_contact)
        db.commit()
        db.refresh(db_contact)
        return db_contact
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Contact already exists"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating contact"
        )
