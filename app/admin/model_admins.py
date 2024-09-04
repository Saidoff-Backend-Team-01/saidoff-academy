
from sqladmin import Admin, ModelView
from app.models.banner import Banner

class BannerAdmin(ModelView, model=Banner):
    column_list = [Banner.id, Banner.title, Banner.desc]
    form_columns = [Banner.id, Banner.title, Banner.desc]
    column_searchable_list = [Banner.title]


