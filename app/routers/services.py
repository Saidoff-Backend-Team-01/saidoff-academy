from typing import List

from fastapi import APIRouter, Depends, HTTPException

from watchfiles import awatch

from app.schemas.services import ServicesListSchema, ServicesCreateSchema
from app.crud.services import *
from app.config.database import SessionLocal, get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/services",
    tags=["Services"]
)


@router.post("/create_services", response_model=ServicesListSchema)
def create_new_services(services: ServicesCreateSchema, db: Session = Depends(get_db)):
    try:
        return create_services(db, services)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/", response_model=List[ServicesListSchema])
def read_services(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    services = db.query(OurServices).offset(skip).limit(limit).all()
    return services


@router.get("/{slug}", response_model=ServicesListSchema)
def read_service(slug: str, db: Session = Depends(get_db)):
    service = get_services(slug, db)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service
