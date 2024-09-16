from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, Query


from app.crud.faq import get_faq
from app.schemas.faq import FaqListSchemas
from app.config.database import SessionLocal, get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/Faq",
    tags=["FAQ"]
)


# @router.get("/", response_model=List[FaqListSchemas])
# def get_faq_list(db: Session = Depends(get_db)):
#     return get_faq_list(db)

@router.get("/", response_model=List[FaqListSchemas])
def read_faqs(
    faq_type: Optional[str] = Query(None, description="FAQ turi buyicha filter"),
    db: Session = Depends(get_db)
):
    return get_faq(db, faq_type=faq_type)
