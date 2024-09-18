from pydantic import BaseModel


class SocilaMediaModel(BaseModel):
    image: str
    link: str

    def return_data(self) -> str:
        base_url = 'http://127.0.0.1:8005'
        image_url =  f'{base_url}/{self.image}'
        url = self.link

        return {'image': image_url, 'link': url}
    
    class Config:
        orm_mode = True