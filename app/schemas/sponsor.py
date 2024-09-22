from pydantic import BaseModel, HttpUrl

from app.config.settings import BASE_URL


class SponsorModel(BaseModel):
    image: str
    url: HttpUrl


    def return_data(self) -> str:
        base_url = BASE_URL
        image_url =  f'{base_url}/{self.image}'
        url = self.url

        return {'image': image_url, 'url': url}
    
    class Config:
        orm_mode = True