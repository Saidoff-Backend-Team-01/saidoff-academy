from fastapi import APIRouter, Depends
from watchfiles import awatch
import uvicorn

from app.crud.ourteam import get_ourteams
from app.schemas.banner import BannerListSchema, BannerCreateSchema
from app.crud.banner import get_banners, create_banner, get_why_we_us
from app.config.database import SessionLocal, get_db
from sqlalchemy.orm import Session

from app.schemas.ourteam import OurteamCreateSchema

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


@router.get("/why_we_us/")
async def why_we_us(db: Session = Depends(get_db)):
    return get_why_we_us(db)

if __name__ == '__main__':
    uvicorn.run
