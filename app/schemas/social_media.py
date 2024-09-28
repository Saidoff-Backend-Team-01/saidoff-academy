from pydantic import BaseModel

from app.config.settings import BASE_URL

class SocilaMediaModel(BaseModel):
    image: str
    link: str

    def return_data(self) -> str:
        base_url = BASE_URL
        image_url =  f'{base_url}/{self.image}'
        url = self.link

        return {'image': image_url, 'link': url}
    
    class Config:
        orm_mode = True