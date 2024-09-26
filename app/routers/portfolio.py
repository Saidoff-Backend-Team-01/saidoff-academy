from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.crud.portfolio import categories_get, item_get, item_filter_get
from app.schemas.portfolio import PortfolioCategoryModel, PortfolioItemModel
from app.config.database import get_db

from typing import Optional, List


router = APIRouter(prefix='/portfolio')


@router.get('/category', response_model=list[PortfolioCategoryModel])
async def category_view(db: Session = Depends(get_db)):
    return categories_get(db=db)


@router.get('/portfolio', response_model=list[PortfolioItemModel])
async def portfolio_view(db: Session = Depends(get_db), tags: Optional[List[str]] = Query(None)):
    return item_get(db=db, tags=tags)


@router.get('/portfolio/{category}', response_model=list[PortfolioItemModel])
async def portfolio_filter_view(category: str, db: Session = Depends(get_db)):
    return item_filter_get(db=db, category=category)