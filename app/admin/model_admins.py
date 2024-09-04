from sqladmin import Admin, ModelView
from app.models.common import Banner

class BannerAdmin(ModelView, model=Banner):
    column_list = [Banner.id, Banner.title, Banner.desc]
    form_columns = [Banner.id, Banner.title, Banner.desc, Banner.email, Banner.phone, Banner.image]
    column_searchable_list = [Banner.title]