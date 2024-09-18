from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from sqlalchemy.exc import IntegrityError

from app.models.faq import Faq, FaqType
from app.schemas.faq import FaqCreateSchemas


# def get_faq(db: Session):
#     return db.query(Faq).all()

def get_faq(db: Session, faq_type: Optional[str] = None):
    query = db.query(Faq)

    if faq_type:
        try:
            faq_type_enum = FaqType(faq_type)
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid faq_type value"
            )
        query = query.filter(Faq.faq_type == faq_type_enum)

    return query.all()

# def create_faq(db: Session, faq: FaqCreateSchemas):
#     new_faq = Faq(
#         question=faq.question,
#  git lo       answer=faq.answer,
#         faq_type=faq.faq_type
#     )
#     db.add(new_faq)
#     db.commit()
#     db.refresh(new_faq)
#     return new_faq


def create_faq(db: Session, faq: FaqCreateSchemas):
    if faq.faq_type and faq.faq_type not in [e.value for e in FaqType]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid faq_type value"
        )

    new_faq = Faq(
        question=faq.question,
        answer=faq.answer,
        faq_type=FaqType(faq.faq_type) if faq.faq_type else None
    )

    try:
        db.add(new_faq)
        db.commit()
        db.refresh(new_faq)
        return new_faq
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="FAQ already exists"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error creating FAQ"
        )

