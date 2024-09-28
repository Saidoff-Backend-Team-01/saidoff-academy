from typing import List
from fastapi import FastAPI
from typing_extensions import Optional
import uvicorn
from fastapi.staticfiles import StaticFiles

from app.config.database import Base, SessionLocal, engine, get_db


from fastapi import FastAPI, Request
from babel import Locale
from babel.support import Translations

from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from . import models, crud
from app.routers.translations import router as translations_router


from app.routers.company import router as company_router
from app.routers.services import router as service_router

from app.routers.company import router as company_router

from app.routers.ourteam import router as our_team_router
from app.routers.services import router as services_router
from app.routers.faq import router as faq_router
from app.routers.social_media import router as social_media_router
from app.routers.sponsors import router as sponsors_router
from app.routers.contactwithus import router as contact_router
from app.routers.why_we_us import router as why_we_us_router
from app.routers.portfolio import router as portfolio_router
from app.routers.config import router as config_router
from sqladmin import Admin, ModelView
from app.admin import model_admins
from app.admin.auth import authentication_backend
from app.config.settings import base_settings


sponsors_router
app = FastAPI(
    prefix='/api/v1/'
)

admin = Admin(app, engine, authentication_backend=authentication_backend)

translations = Translations.load('translations', locales=['en', 'es'])

admin.add_view(model_admins.BannerAdmin)
# admin.add_view(model_admins.Why_we_us_Admin)
# admin.add_view(model_admins.Service_Admin)
admin.add_view(model_admins.Why_we_usAdmin)
admin.add_view(model_admins.FeatureAdmin)
admin.add_view(model_admins.PlanAdmin)
admin.add_view(model_admins.ConfigAdmin)
admin.add_view(model_admins.FaqAdmin)
admin.add_view(model_admins.ContactWithUsAdmin)
admin.add_view(model_admins.FeedbacksAdmin)
admin.add_view(model_admins.OurServiceInfoAdmin)
admin.add_view(model_admins.SocialMediasAdmin)
admin.add_view(model_admins.PortfolioCategoryAdmin)
admin.add_view(model_admins.PortfolioItemAdmin)
admin.add_view(model_admins.PortfolioTagAdmin)
admin.add_view(model_admins.OurteamAdmin)
admin.add_view(model_admins.ServicesAdmin)
admin.add_view(model_admins.SponsorAdmin)


app.include_router(company_router)
app.include_router(our_team_router)
app.include_router(services_router)
app.include_router(faq_router)
app.include_router(contact_router)
app.include_router(social_media_router)
app.include_router(sponsors_router)
app.include_router(contact_router)
app.include_router(translations_router)



# app = FastAPI()
#
# @app.middleware("http")
# async def set_language_locale(request: Request, call_next):
#     lang = request.headers.get('Accept-Language', 'en')
#     locale = Locale.parse(lang, sep='-')
#
#     request.state.locale = locale
#     request.state.translations = translations
#     response = await call_next(request)
#     return response
#

# app.include_router(why_we_us_router)
# app.include_router(portfolio_router)
# app.include_router(config_router)

app.mount("/media", StaticFiles(directory="media"), name="media")

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

