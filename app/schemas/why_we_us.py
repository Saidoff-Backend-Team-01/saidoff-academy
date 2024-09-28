from pydantic import BaseModel

from app.config.settings import BASE_URL


class WhyWeUSModel(BaseModel):
    id: int
    title: str
    desc: str
    image: str

    def return_data(self) -> str:
        base_url = BASE_URL
        image_url =  f'{base_url}/{self.image}'
  

        return {'id': self.id, 'title': self.title, 'desc': self.desc, 'image': image_url}