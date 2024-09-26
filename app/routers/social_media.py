from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.social_media import SocilaMediaModel
from app.crud.social_media import get_socialmedia
from app.config.database import get_db


router = APIRouter(prefix='/social')


@router.get('/socilamedia', response_model=list[SocilaMediaModel])
async def social_media_get(db: Session = Depends(get_db)):
    return get_socialmedia(db=db)