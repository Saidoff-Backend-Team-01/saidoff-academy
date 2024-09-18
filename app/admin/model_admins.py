from sqladmin import Admin, ModelView


from app.models.our_team import OurTeam
from app.models.our_services import OurServices, OurServiceInfo
from app.models.banner import Banner
from app.models.why_we_us import WhyWeUs
from app.models.plan import Plan, Feature
from app.models.config import Config
from app.models.faq import Faq
from app.models.contact_with_us import ContactWithUs
from app.models.customer_feedback import Feedbacks
from app.models.our_team import OurTeam
from app.models.social_medias import SocialMedias
from app.models.portfolio import PortfolioCategory, PortfolioItem




class BannerAdmin(ModelView, model=Banner):
    column_list = [Banner.id, Banner.title, Banner.desc]
    form_columns = [Banner.id, Banner.title, Banner.desc, Banner.page_type]
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


class PlanAdmin(ModelView, model=Plan):
    column_list = [Plan.id, Plan.name]
    form_columns = [Plan.name, Plan.price, Plan.is_popular, Plan.desc, Plan.features]


class FeatureAdmin(ModelView, model=Feature):
    column_list = [Feature.id, Feature.name]
    form_columns = [Feature.name, Feature.plan_id, Feature.plans]


