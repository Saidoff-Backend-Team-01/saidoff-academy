
from sqladmin import Admin, ModelView
from app.models.company import Banner

class BannerAdmin(ModelView, model=Banner):
    column_list = [Banner.id, Banner.title, Banner.desc]
    form_columns = [Banner.id, Banner.title, Banner.desc]
    column_searchable_list = [Banner.title]



class Why_we_usAdmin(ModelView, model=Why_we_us):
    column_list = [Why_we_us.id, Why_we_us.title, Why_we_us.desc]