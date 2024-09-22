from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile


from app.schemas.ourteam import OurteamListSchema, OurteamCreateSchema
from app.crud.ourteam import get_ourteams, create_ourteam
from app.config.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/ourteam",
    tags=["Our_Team"]
)


@router.get("/", response_model=List[OurteamListSchema])
def get_ourteam_list(db: Session = Depends(get_db)):
    ourteam = get_ourteams(db)

    return [OurteamListSchema(id=member.id, name=member.name, image=member.image, position=member.position, experience=member.experience).return_data() for member in ourteam]

