
from sqladmin import Admin, ModelView
from app.models.company import Banner, Why_we_us
from app.models.services import Service


# from app.models.faq import Faq
from app.models.our_team import OurTeam
from app.models.our_services import OurServices
# from app.models.faq import Faq
from app.models.banner import Banner, Why_we_us



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


class OurteamAdmin(ModelView, model=OurTeam):
    column_list = [OurTeam.id, OurTeam.name, OurTeam.position]
    form_columns = [OurTeam.id, OurTeam.name, OurTeam.position]
    column_searchable_list = [OurTeam.name]


class ServicesAdmin(ModelView, model=OurServices):
    column_list = [OurServices.id, OurServices.title, OurServices.desc]
    form_columns = [OurServices.id, OurServices.title, OurServices.desc]
    column_searchable_list = [OurServices.title]



class Why_we_usAdmin(ModelView, model=Why_we_us):
    column_list = [Why_we_us.id, Why_we_us.title, Why_we_us.desc]
