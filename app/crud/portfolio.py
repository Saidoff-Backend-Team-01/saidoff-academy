from sqlalchemy.orm import Session

from app.models.portfolio import PortfolioCategory, PortfolioItem, PortfolioTag



def categories_get(db: Session):
    categories = db.query(PortfolioCategory).all()

    return categories


def item_get(db: Session, tags):
    if tags is None:
        items = db.query(PortfolioItem).all()
        return items
    
    for i in tags:
        items = db.query(PortfolioItem).filter(PortfolioItem.tags.any(PortfolioTag.name == i)).all()

    return items


def item_filter_get(db: Session, category):
    items = db.query(PortfolioItem).join(PortfolioCategory).filter(PortfolioCategory.name == category).all()

    return items