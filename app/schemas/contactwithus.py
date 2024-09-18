from pydantic import BaseModel
from typing import Optional


class ContactWithUsListSchema(BaseModel):
    id: int
    name: str
    pthone_number: int
    category_id: int
    desc: str


class ContactWithUsSchema(BaseModel):
    name: str
    phone_number: int
    category_id: int
    desc: str

    class Config:
        orm_mode = True

