from fastapi import APIRouter, Depends
from app.schemas.why_we_us import WhyWeUSModel
from app.crud.why_we_us import whywe_get
from app.config.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix='/why_we_us')


@router.get('/why_we', response_model=list[WhyWeUSModel])
def why_we_view(db: Session = Depends(get_db)):
    why_we =  whywe_get(db=db)

    return [WhyWeUSModel(id=why.id, title=why.title, desc=why.desc, image=why.bg_image).return_data() for why in why_we]