from fastapi import APIRouter, Depends
from watchfiles import awatch
import uvicorn

from app.schemas.banner import BannerListSchema, BannerCreateSchema
from app.crud.service import get_services
from app.config.database import SessionLocal, get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/service"
)


@router.get("/service/")
async def service(db: Session = Depends(get_db)):
    return get_services(db)


if __name__ == '__main__':
    uvicorn.run