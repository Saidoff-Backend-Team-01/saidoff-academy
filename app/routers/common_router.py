from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.common_schemas import SocilaMediaModel
from app.crud.common_crud import get_socialmedia
from app.config.database import get_db


router = APIRouter(prefix='/common')


@router.get('/socilamedia', response_model=list[SocilaMediaModel])
def social_media_get(db: Session = Depends(get_db)):
    return get_socialmedia(db=db)