from pydantic import BaseModel
from typing import List, Optional


class PortfolioCategoryModel(BaseModel):
    id: int
    name: str


class PortfolioTagModel(BaseModel):
    id: int
    name: str


class PortfolioItemModel(BaseModel):
    id: int
    title: str
    image: str
    category_id: int

    category: PortfolioCategoryModel
    tags: Optional[List[PortfolioTagModel]] = []