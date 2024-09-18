
from sqladmin import Admin, ModelView
from app.models.banner import Banner
from app.models.why_we_us import WhyWeUs
from app.models.our_services import OurServices
<<<<<<< HEAD
from app.models.our_team import OurTeam
=======
# from app.models.faq import Faq
from app.models.banner import Banner
from app.models.why_we_us import WhyWeUs


>>>>>>> 634d1187a51850019666e0e4f130ef69763c4d5f

class BannerAdmin(ModelView, model=Banner):
    column_list = [Banner.id, Banner.title, Banner.desc]
    form_columns = [Banner.id, Banner.title, Banner.desc, Banner.bg_image, Banner.phone_num]
    column_searchable_list = [Banner.title]


class WhyWeUs_Admin(ModelView, model=WhyWeUs):
    column_list = [WhyWeUs.id, WhyWeUs.title, WhyWeUs.desc]
    form_columns = [WhyWeUs.id, WhyWeUs.title, WhyWeUs.desc]
    column_searchable_list = [WhyWeUs.title]
    
    
class OurServices_Admin(ModelView, model=OurServices):
    column_list = [OurServices.id, OurServices.title, OurServices.desc]
    form_columns = [OurServices.id, OurServices.title, OurServices.desc]
    column_searchable_list = [OurServices.title]


class OurteamAdmin(ModelView, model=OurTeam):
    column_list = [OurTeam.id, OurTeam.name, OurTeam.position]
    form_columns = [OurTeam.id, OurTeam.name, OurTeam.position]
    column_searchable_list = [OurTeam.name]

class OurServicessAdmin(ModelView, model=OurServices):
    column_list = [OurServices.id, OurServices.title, OurServices.desc]
    form_columns = [OurServices.id, OurServices.title, OurServices.desc]
    column_searchable_list = [OurServices.title]

<<<<<<< HEAD
class WhyWeUsAdmin(ModelView, model=WhyWeUs):
=======


class Why_we_usAdmin(ModelView, model=WhyWeUs):
>>>>>>> 634d1187a51850019666e0e4f130ef69763c4d5f
    column_list = [WhyWeUs.id, WhyWeUs.title, WhyWeUs.desc]
