from pydantic import BaseModel
from typing import Optional


class ContactWithUsListSchema(BaseModel):
    name: str
    phone_number: str
    service_type: int
    msg: str


class ContactWithUsSchema(BaseModel):
    name: str
    phone_number: str
    service_type: int
    msg: str

    class Config:
        orm_mode = True

