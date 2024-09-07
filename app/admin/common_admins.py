from sqladmin import Admin, ModelView
from app.models.common import Banner, SocialMedia

class BannerAdmin(ModelView, model=Banner):
    name = 'Banner'
    name_plural = 'Banners'

    column_list = [Banner.id, Banner.title, Banner.desc]
    form_columns = [Banner.id, Banner.title, Banner.desc, Banner.email, Banner.phone, Banner.image]
    column_searchable_list = [Banner.title]

class SocialMediaAdmin(ModelView, model=SocialMedia):
    name = 'Social media'
    name_plural = 'Social media'

    column_list = [SocialMedia.id, SocialMedia.facebook_url]
    form_columns = [SocialMedia.id, SocialMedia.facebook_url, SocialMedia.vimeo_url, SocialMedia.facebook_url, SocialMedia.twitter_url, SocialMedia.youtube_url]
