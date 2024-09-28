from fastapi import APIRouter, Depends

from app.crud.ourteam import get_ourteams

from app.schemas.banner import BannerListSchema, BannerCreateSchema
from app.crud.banner import *
from app.schemas.banner import BannerListSchema, BannerCreateSchema
from app.schemas.custumer_feedback import CustomerFeedbackSchema
from app.crud.banner import get_banners, get_customer_feedbacks
from app.config.database import SessionLocal, get_db
from sqlalchemy.orm import Session
from typing import List
from fastapi import FastAPI, Depends, HTTPException, Query



router = APIRouter(
    prefix="/company"
)

@router.get("/banners", response_model=list[BannerListSchema])
async def banners(db: Session = Depends(get_db)):
    return get_banners(db)

@router.get("/why_we_us/")
async def why_we_us(db: Session = Depends(get_db)):
    return get_why_we_us(db)

@router.get("/feedbacks/")
def read_feedbacks(db: Session = Depends(get_db)):
    feedbacks = get_customer_feedbacks(db)
    return [CustomerFeedbackSchema(id=feedback.id, name=feedback.name, position=feedback.position, image=feedback.image, feedback_text=feedback.feedback_text).return_data() for feedback in feedbacks]
