from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, Query


from app.crud.faq import get_faq, create_faq
from app.schemas.faq import FaqListSchemas, FaqCreateSchemas
from app.config.database import SessionLocal, get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/Faq",
    tags=["FAQ"]
)


@router.get("/", response_model=List[FaqListSchemas])
def read_faqs(
    faq_type: Optional[str] = Query(None, description="FAQ turi bo'yicha filtr"),
    db: Session = Depends(get_db)
):
    try:
        faqs = get_faq(db, faq_type=faq_type)
        if not faqs:
            raise HTTPException(status_code=404, detail="No FAQs found")
        return faqs
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

