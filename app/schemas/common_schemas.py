from pydantic import BaseModel


class SocilaMediaModel(BaseModel):
    facebook_url: str
    twitter_url: str
    vimeo_url: str
    youtube_url: str
    