from pydantic import BaseModel, HttpUrl
from typing import Optional, List


class OurteamListSchema(BaseModel):
    id: int
    name: str
    image: str
    position: str


class OurteamCreateSchema(BaseModel):
    name: str
    image: str
    position: Optional[str] = None
    experience: str

    class Config:
        orm_mode = True
