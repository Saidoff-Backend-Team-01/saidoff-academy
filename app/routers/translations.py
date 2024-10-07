from typing import List, Optional
from fastapi import APIRouter, Depends, Request, HTTPException
from app.crud import translation
from app.config.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/translations",
    tags=["Translations"],
)


@router.post("/items/")
async def create_item(name: str, description: str, translations: List[dict], db: Session = Depends(get_db)):
    new_item = translation.create_item(db, name, description, translations)
    return {"status": "success", "item_id": new_item.id}


@router.get("/items/{item_id}")
async def get_item(item_id: int, request: Request, db: Session = Depends(get_db)):
    lang = request.headers.get('Accept-Language', 'en')
    item = translation.get_item(db, item_id, lang)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get("/greet/")
async def greet(request: Request):
    _ = request.state.translations.gettext
    greeting = _("Hello!")
    return {"greeting": greeting}
