from fastapi import APIRouter, Depends


from app.schemas.banner import BannerListSchema, BannerCreateSchema
from app.config.database import SessionLocal, get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/company"
)

@router.get("/banners")
async def banners(db: Session = Depends(get_db)):
    ...


@router.post("/banner")
async def banner_create(banner: BannerCreateSchema, db: Session = Depends(get_db)):
    ...
