
from sqladmin import Admin, ModelView

from app.models.banner import Banner
from app.models.ourteam import Ourteam
from app.models.our_services import OurServices

from app.models.banner import Banner, Why_we_us


class BannerAdmin(ModelView, model=Banner):
    column_list = [Banner.id, Banner.title, Banner.desc]
    form_columns = [Banner.id, Banner.title, Banner.desc]
    column_searchable_list = [Banner.title]


class OurteamAdmin(ModelView, model=Ourteam):
    column_list = [Ourteam.id, Ourteam.name, Ourteam.position]
    form_columns = [Ourteam.id, Ourteam.name, Ourteam.position]
    column_searchable_list = [Ourteam.name]


class ServicesAdmin(ModelView, model=OurServices):
    column_list = [OurServices.id, OurServices.title, OurServices.desc]
    form_columns = [OurServices.id, OurServices.title, OurServices.desc]
    column_searchable_list = [OurServices.title]


class Why_we_usAdmin(ModelView, model=Why_we_us):
    column_list = [Why_we_us.id, Why_we_us.title, Why_we_us.desc]
