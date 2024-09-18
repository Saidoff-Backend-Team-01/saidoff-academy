
from sqladmin import Admin, ModelView

# from app.models.faq import Faq
from app.models.our_team import OurTeam
from app.models.our_services import OurServices
# from app.models.faq import Faq
from app.models.banner import Banner
from app.models.why_we_us import WhyWeUs
from app.models.portfolio import *
from app.models.contact_with_us import ContactWithUs


class BannerAdmin(ModelView, model=Banner):
    column_list = [Banner.id, Banner.title, Banner.desc]
    form_columns = [Banner.id, Banner.title, Banner.desc, Banner.bg_image, Banner.phone_num]
    column_searchable_list = [Banner.title]


class OurteamAdmin(ModelView, model=OurTeam):
    column_list = [OurTeam.id, OurTeam.name, OurTeam.position]
    form_columns = [OurTeam.id, OurTeam.name, OurTeam.position]
    column_searchable_list = [OurTeam.name]


class ServicesAdmin(ModelView, model=OurServices):
    column_list = [OurServices.id, OurServices.title, OurServices.desc]
    form_columns = [OurServices.id, OurServices.title, OurServices.desc]
    column_searchable_list = [OurServices.title]


class Why_we_usAdmin(ModelView, model=WhyWeUs):
    column_list = [WhyWeUs.id, WhyWeUs.title, WhyWeUs.desc]


class PortfolioCategoryAdmin(ModelView, model=PortfolioCategory):
    column_list = [PortfolioCategory.id, PortfolioCategory.name]
    form_columns = [PortfolioCategory.id, PortfolioCategory.name]


class ContactwithAdmin(ModelView, model=ContactWithUs):
    column_list = [ContactWithUs.id, ContactWithUs.name]
    form_columns = [ContactWithUs.id, ContactWithUs.name]
