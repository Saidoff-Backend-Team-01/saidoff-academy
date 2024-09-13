
from sqladmin import Admin, ModelView
from app.models.company import Banner, Why_we_us
from app.models.services import Service


class BannerAdmin(ModelView, model=Banner):
    column_list = [Banner.id, Banner.title, Banner.desc]
    form_columns = [Banner.id, Banner.title, Banner.desc]
    column_searchable_list = [Banner.title]


class Why_we_us_Admin(ModelView, model=Why_we_us):
    column_list = [Why_we_us.id, Why_we_us.title, Why_we_us.desc]
    form_columns = [Why_we_us.id, Why_we_us.title, Why_we_us.desc]
    column_searchable_list = [Why_we_us.title]
    
    
class Service_Admin(ModelView, model=Service):
    column_list = [Service.id, Service.title, Service.desc]
    form_columns = [Service.id, Service.title, Service.desc]
    column_searchable_list = [Service.title]