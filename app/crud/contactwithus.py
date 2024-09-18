from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from sqlalchemy.exc import IntegrityError

from app.models.contact_with_us import ContactWithUs
from app.schemas.contactwithus import ContactWithUsSchema
from app.models.portfolio import PortfolioCategory


def create_contact(db: Session, contact: ContactWithUsSchema):
    category = db.query(PortfolioCategory).filter(PortfolioCategory.id == contact.category_id).first()

    if not category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid category_id"
        )

    db_contact = ContactWithUs(**contact.dict())
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
