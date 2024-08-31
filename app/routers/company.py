from fastapi import APIRouter, Depends
from watchfiles import awatch

from app.schemas.banner import BannerListSchema, BannerCreateSchema
from app.crud.banner import get_banners, create_banner
from app.config.database import SessionLocal, get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/company"
)


@router.get("/banners")
async def banners(db: Session = Depends(get_db)):
    return get_banners(db)


@router.post("banner/")
async def banner_create(banner: BannerCreateSchema, db: Session = Depends(get_db)):
    new_banner = create_banner(banner_create=banner, db=db)
    return new_banner
