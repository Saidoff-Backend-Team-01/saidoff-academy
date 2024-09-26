from pydantic import BaseModel, HttpUrl
from typing import Optional, List

from app.config.settings import BASE_URL


class OurteamListSchema(BaseModel):
    id: int
    name: str
    image: str
    position: str
    experience: str

    def return_data(self) -> str:
        base_url = BASE_URL
        image_url =  f'{base_url}/{self.image}'


        return {'id': self.id, 'position': self.position, 'name': self.name, 'image': image_url, 'experience': self.experience}


class OurteamCreateSchema(BaseModel):
    name: str
    image: str
    position: Optional[str] = None
    experience: str
    

    class Config:
        orm_mode = True
