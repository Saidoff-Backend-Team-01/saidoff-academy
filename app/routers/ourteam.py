from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from typer import models

from watchfiles import awatch

from app.crud.services import create_services
from app.schemas.ourteam import OurteamListSchema, OurteamCreateSchema
from app.crud.ourteam import get_ourteams, create_ourteam
from app.config.database import SessionLocal, get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/ourteam",
    tags=["Our_Team"]
)


@router.get("/", response_model=List[OurteamListSchema])
def get_ourteam_list(db: Session = Depends(get_db)):
    return get_ourteams(db)


@router.post("/create_ourteam", response_model=OurteamListSchema)
def create_new_ourteam(ourteam: OurteamCreateSchema, db: Session = Depends(get_db)):
    try:
        return create_ourteam(db, ourteam)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")