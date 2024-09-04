import uvicorn
from fastapi import FastAPI
from app.config.database import engine

from app.routers.company import router as company_router
from sqladmin import Admin
from app.admin import model_admins
from app.admin.auth import authentication_backend
from fastapi.staticfiles import StaticFiles



app = FastAPI(
    prefix='/api/v1/'
)

admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(model_admins.BannerAdmin)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(company_router)

if __name__ == '__main__':
    uvicorn.run('main:app', port=8005, reload=True)


