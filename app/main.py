from typing import List
from fastapi import FastAPI
from typing_extensions import Optional
import uvicorn

from app.config.database import Base, SessionLocal, engine, get_db

from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from . import models, crud

from app.routers.company import router as company_router
from app.routers.ourteam import router as our_team_router
from app.routers.services import router as services_router
from app.routers.faq import router as faq_router
from app.routers.contact import router as contact_router
from app.routers.social_media import router as social_media_router
from app.routers.sponsors import router as sponsors_router
from app.routers.contactwithus import router as contact_router
from sqladmin import Admin, ModelView
from app.admin import model_admins
from app.admin.auth import authentication_backend
from app.config.settings import base_settings


app = FastAPI(
    prefix='/api/v1/'
)

admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(model_admins.BannerAdmin)
admin.add_view(model_admins.Why_we_usAdmin)


app.include_router(company_router)
app.include_router(our_team_router)
app.include_router(services_router)
app.include_router(faq_router, prefix='/api/v1')
app.include_router(contact_router)
app.include_router(social_media_router)
app.include_router(sponsors_router)
app.include_router(contact_router)


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post("/items/")
async def create_item(name: str, description: str, translations: list, db: Session = Depends(get_db)):
    new_item = crud.create_item(db, name, description, translations)
    return {"status": "success", "item_id": new_item.id}


@app.get("/items/{item_id}")
async def get_item(item_id: int, request: Request, db: Session = Depends(get_db)):
    locale = request.headers.get('Accept-Language', 'en')
    item = crud.get_item(db, item_id, locale)
    return item



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)