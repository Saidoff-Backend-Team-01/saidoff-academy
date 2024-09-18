from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.schemas.contact import ContactUSModel
from app.config.database import get_db
from app.crud.contact import post_contact_us


router = APIRouter(prefix='/contact')


@router.post('/contactus', response_model=ContactUSModel)
def create_contact_us(contact_us: ContactUSModel, db: Session = Depends(get_db)):
    return post_contact_us(db=db, contact=contact_us)
