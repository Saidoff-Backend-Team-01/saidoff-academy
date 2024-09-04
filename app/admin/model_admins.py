
from sqladmin import Admin, ModelView
from app.models.company import Banner
from app.models.ourteam import Ourteam
from app.models.services import Services


class BannerAdmin(ModelView, model=Banner):
    column_list = [Banner.id, Banner.title, Banner.desc]
    form_columns = [Banner.id, Banner.title, Banner.desc]
    column_searchable_list = [Banner.title]


class OurteamAdmin(ModelView, model=Ourteam):
    column_list = [Ourteam.id, Ourteam.name, Ourteam.position]
    form_columns = [Ourteam.id, Ourteam.name, Ourteam.position]
    column_searchable_list = [Ourteam.name]


class ServicesAdmin(ModelView, model=Services):
    column_list = [Services.id, Services.title, Services.desc]
    form_columns = [Services.id, Services.title, Services.desc]
    column_searchable_list = [Services.title]

