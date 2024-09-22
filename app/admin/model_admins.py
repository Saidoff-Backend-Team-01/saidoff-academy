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
from app.models.portfolio import PortfolioCategory, PortfolioItem, PortfolioTag
from app.models.sponsors import Sponsors



class BannerAdmin(ModelView, model=Banner):
    column_list = [Banner.id, Banner.title, Banner.desc]
    form_columns = [Banner.id, Banner.title, Banner.desc, Banner.page_type]
    column_searchable_list = [Banner.title]



class OurteamAdmin(ModelView, model=OurTeam):
    column_list = [OurTeam.id, OurTeam.name, OurTeam.position]
    form_columns = [OurTeam.id, OurTeam.name, OurTeam.position, OurTeam.image, OurTeam.experience]
    column_searchable_list = [OurTeam.name]


class ServicesAdmin(ModelView, model=OurServices):
    column_list = [OurServices.id, OurServices.title, OurServices.desc]
    form_columns = [OurServices.id, OurServices.title, OurServices.desc, OurServices.image, OurServices.slug, OurServices.service_infos]
    column_searchable_list = [OurServices.title]



class Why_we_usAdmin(ModelView, model=WhyWeUs):
    column_list = [WhyWeUs.id, WhyWeUs.title, WhyWeUs.desc]


class PlanAdmin(ModelView, model=Plan):
    column_list = [Plan.id, Plan.name]
    form_columns = [Plan.name, Plan.price, Plan.is_popular, Plan.desc, Plan.features]


class FeatureAdmin(ModelView, model=Feature):
    column_list = [Feature.id, Feature.name]
    form_columns = [Feature.name, Feature.plan_id, Feature.plans]


class ConfigAdmin(ModelView, model=Config):
    column_list = [Config.id, Config.email, Config.phone]
    form_columns = [Config.email, Config.phone]


class FaqAdmin(ModelView, model=Faq):
    column_list = [Faq.id, Faq.faq_type]
    form_columns = [Faq.faq_type, Faq.question, Faq.answer, Faq.order]


class ContactWithUsAdmin(ModelView, model=ContactWithUs):
    can_create = False
    can_delete = False
    can_edit =False
    column_list = [ContactWithUs.id, ContactWithUs.name, ContactWithUs.phone_number]
    form_columns = [ContactWithUs.id, ContactWithUs.name, ContactWithUs.phone_number]
 

class FeedbacksAdmin(ModelView, model=Feedbacks):
    column_list = [Feedbacks.id, Feedbacks.name, Feedbacks.position]
    form_columns = [Feedbacks.name, Feedbacks.image, Feedbacks.feedback_text, Feedbacks.position]


class OurServiceInfoAdmin(ModelView, model=OurServiceInfo):
    column_list = [OurServiceInfo.id]
    form_columns = [OurServiceInfo.additional_info, OurServiceInfo.service_id, OurServiceInfo.service]


class SocialMediasAdmin(ModelView, model=SocialMedias):
    column_list = [SocialMedias.id, SocialMedias.image, SocialMedias.link]
    form_columns = [SocialMedias.image, SocialMedias.link]


class PortfolioCategoryAdmin(ModelView, model=PortfolioCategory):
    column_list = [PortfolioCategory.id, PortfolioCategory.name]
    form_columns = [PortfolioCategory.name, PortfolioCategory.items]


class PortfolioItemAdmin(ModelView, model=PortfolioItem):
    column_list = [PortfolioItem.id, PortfolioItem.title]
    form_columns = [PortfolioItem.title, PortfolioItem.image, PortfolioItem.category_id, PortfolioItem.category, PortfolioItem.tags]


class PortfolioTagAdmin(ModelView, model=PortfolioTag):
    column_list = [PortfolioTag.id, PortfolioTag.name]
    form_columns = [PortfolioTag.name, PortfolioTag.item]


class PortfolioTagAdmin(ModelView, model=Sponsors):
    column_list = [Sponsors.id]
    form_columns = [Sponsors.url, Sponsors.image]