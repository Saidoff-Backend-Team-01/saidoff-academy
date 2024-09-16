from typing import List
from fastapi import FastAPI
from typing_extensions import Optional
import uvicorn

from app.config.database import Base, SessionLocal, engine

# from app.routers.company import router as company_router
from app.routers.ourteam import router as our_team_router
from app.routers.services import router as services_router
from app.routers.faq import router as faq_router
from app.routers.contact import router as contact_router
from app.routers.social_media import router as social_media_router
from app.routers.sponsors import router as sponsors_router
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


# app.include_router(company_router)
app.include_router(our_team_router)
app.include_router(services_router)
app.include_router(faq_router, prefix='/api/v1')
app.include_router(contact_router)
app.include_router(social_media_router)
app.include_router(sponsors_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)