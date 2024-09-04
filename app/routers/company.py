from fastapi import APIRouter, Depends
from watchfiles import awatch

from app.crud.ourteam import get_ourteams
from app.schemas.banner import BannerListSchema, BannerCreateSchema
from app.crud.banner import get_banners, create_banner
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


# @router.get("/ourteams")
# async def ourteam(db: Session = Depends(get_db)):
#     return get_ourteams(db)
#
#
# @router.post("/create_ourteam")
# async def ourteam_create(banner: OurteamCreateSchema, db: Session = Depends(get_db)):
#     new_ourteam = ourteam_create(ourteam_create=ourteam, db=db)
#     return new_ourteam


# @router.put("/items/{item_id}")
# async def update_ourteam(item_id: int, item: ourteam):
#     results = {"item_id": item_id, "item": item}
#     return results
