from pydantic import BaseModel

from app.config.settings import BASE_URL


class ServicesListSchema(BaseModel):
    id: int
    title: str
    desc: str
    slug: str
    image: str

    def return_data(self) -> str:
        base_url = BASE_URL
        image_url =  f'{base_url}/{self.image}'
        

        return {'id': self.id, 'title': self.title, 'desc': self.desc, 'slug': self.slug, 'image': image_url}


class ServicesCreateSchema(BaseModel):
    title: str
    desc: str
    slug: str
    image: str

    class Config:
        orm_mode = True
