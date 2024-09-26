from pydantic import BaseModel

from app.config.settings import BASE_URL

class CustomerFeedbackSchema(BaseModel):
    id: int
    position: str
    name: str
    image: str
    feedback_text: str    

        
    def return_data(self) -> str:
        base_url = BASE_URL
        image_url =  f'{base_url}/{self.image}'
        id = self.id
        name =self.name
        position = self.position
        feedback_text = self.feedback_text

        return {'id': id, 'position': position, 'name': name, 'image': image_url, 'feedback_text': feedback_text}

    class Config:
        orm_mode = True
