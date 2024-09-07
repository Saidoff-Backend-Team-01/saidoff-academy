import uvicorn
from fastapi import FastAPI
from app.config.database import engine

from app.routers.company import router as company_router
from app.routers.custumer_router import router as custumer_router
from app.routers.common_router import router as common_router
from sqladmin import Admin
from app.admin import common_admins, custumer_admins, company_admins
from app.admin.auth import authentication_backend
from fastapi.staticfiles import StaticFiles



app = FastAPI(
    prefix='/api/v1/'
)

admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(common_admins.BannerAdmin)
admin.add_view(common_admins.SocialMediaAdmin)
admin.add_view(custumer_admins.ContactUSAdmin)
admin.add_view(custumer_admins.FeedbackAdmin)
admin.add_view(company_admins.SponsorkAdmin)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(custumer_router)
app.include_router(common_router)
app.include_router(company_router)

if __name__ == '__main__':
    uvicorn.run('main:app', port=8005, reload=True)


