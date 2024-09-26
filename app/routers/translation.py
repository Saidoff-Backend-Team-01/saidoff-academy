from typing import List, Optional


from fastapi import APIRouter, Depends, HTTPException, UploadFile, Query
from fastapi import Request

from app.crud import translation
from app.config.database import SessionLocal, get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/Translation",
    tags=["Translations"],
)


@router.post("/items/")
async def create_item(name: str, description: str, translations: list, db: Session = Depends(get_db)):
    new_item = translation.create_item(db, name, description, translations)
    return {"status": "success", "item_id": new_item.id}


@router.get("/items/{item_id}")
async def get_item(item_id: int, request: Request, db: Session = Depends(get_db)):
    locale = request.headers.get('Accept-Language', 'en')
    item = translation.get_item(db, item_id, locale)
    return item

# @router.middleware("http")
# async def set_language_locale(request: Request, call_next):
#     # Detect language from request (using headers, query params, etc.)
#     lang = request.headers.get('Accept-Language', 'en')
#     locale = Locale.parse(lang, sep='-')
#
#     # Store the locale in request state for later access
#     request.state.locale = locale
#     request.state.translations = translations
#     response = await call_next(request)
#     return response

