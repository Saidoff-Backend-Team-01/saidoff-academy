from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.schemas.services import ServicesListSchema
from app.crud.services import *
from app.config.database import SessionLocal, get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/services",
    tags=["Services"]
)



@router.get("/", response_model=List[ServicesListSchema])
async def read_services(db: Session = Depends(get_db)):
    services = db.query(OurServices).all()
    return [ServicesListSchema(id=service.id, title=service.title, desc=service.desc, slug=service.slug, image=service.image).return_data() for service in services]


@router.get("/{slug}", response_model=ServicesListSchema)
async def read_service(slug: str, db: Session = Depends(get_db)):
    service = get_services(slug, db)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return ServicesListSchema(id=service.id, title=service.title, desc=service.desc, slug=service.slug, image=service.image).return_data()
