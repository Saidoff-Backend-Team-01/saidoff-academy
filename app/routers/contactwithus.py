from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException


from app.crud.contactwithus import create_contact
from app.schemas.contactwithus import ContactWithUsSchema, ContactWithUsListSchema
from app.config.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/Contact_With_Us",
    tags=["Contact_With_Us"]
)


@router.post("/create_contact")
async def create_new_contact(contact: ContactWithUsSchema, db: Session = Depends(get_db)):
    try:
        return create_contact(db, contact)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
