from sqlalchemy.orm import Session
from typing import Optional

from app.schemas.ourteam import OurteamListSchema, OurteamCreateSchema
from app.models.ourteam import Ourteam


def get_ourteams(db: Session):
    return db.query(Ourteam).all()


def create_ourteam(db: Session, ourteam_create: OurteamCreateSchema):
    db_ourteam = Ourteam(**ourteam_create.dict())
    db.add(db_ourteam)
    db.commit()
    db.refresh(db_ourteam)
    return db_ourteam

