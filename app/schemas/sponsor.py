from pydantic import BaseModel, HttpUrl, root_validator


class SponsorModel(BaseModel):
    image: str
    url: HttpUrl


    def return_data(self) -> str:
        base_url = 'http://127.0.0.1:8005'
        image_url =  f'{base_url}/{self.image}'
        url = self.url

        return {'image': image_url, 'url': url}
    
    class Config:
        orm_mode = True