from typing import List
from fastapi import FastAPI
from app.config.database import Base, SessionLocal, engine

from app.routers.company import router as company_router
from app.routers.service import router as service_router
from sqladmin import Admin, ModelView
from app.admin import model_admins
from app.admin.auth import authentication_backend
from app.config.settings import base_settings

Base.metadata.create_all(bind=engine)

app = FastAPI(
    prefix='/api/v1/'
)

admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(model_admins.BannerAdmin)
admin.add_view(model_admins.Why_we_us_Admin)
admin.add_view(model_admins.Service_Admin)

app.include_router(company_router)
app.include_router(service_router)