from pydantic import BaseModel



class ContactUSModel(BaseModel):
    name: str
    phone: str