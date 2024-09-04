from fastapi import APIRouter, Depends
# from watchfiles import awatch

from app.schemas.banner import BannerListSchema, BannerCreateSchema,PortfolioCategorySchema,PortfolioItemSchema,CustomerFeedbackSchema
from app.crud.banner import get_banners, create_banner, get_portfolio_categories,get_portfolio_items_by_category,get_portfolio_items,get_customer_feedbacks
from app.config.database import SessionLocal, get_db
from sqlalchemy.orm import Session
from typing import List
from fastapi import FastAPI, Depends, HTTPException, Query


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


@router.get("/portfolio/categories/", response_model=List[PortfolioCategorySchema])
async def get_portfolio_categories_list(db: Session = Depends(get_db)):
    categories = get_portfolio_categories(db=db)
    return categories

@router.get("/portfolio-items/", response_model=List[PortfolioItemSchema])
def read_portfolio_items(category_id: int = Query(None), db: Session = Depends(get_db)):
    if category_id:
        items = get_portfolio_items_by_category(db, category_id=category_id)
    else:
        items = get_portfolio_items(db)
    return items


@router.get("/feedbacks/", response_model=List[CustomerFeedbackSchema])
def read_feedbacks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    feedbacks = get_customer_feedbacks(db, skip=skip, limit=limit)
    return feedbacks

