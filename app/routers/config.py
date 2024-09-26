from fastapi import APIRouter, Depends

from app.crud.config import get_config
from app.schemas.config import ConfigModel
from app.config.database import get_db

from sqlalchemy.orm import Session


router = APIRouter(prefix='/config')


@router.get('/config', response_model=ConfigModel)
async def get_config_view(db: Session = Depends(get_db)):
    return get_config(db=db)