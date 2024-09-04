from pydantic import BaseModel, HttpUrl
from typing import Optional, List


class OurteamListSchema(BaseModel):
    id: int
    name: str
    image_data: str
    position: Optional[str] = None


class OurteamCreateSchema(BaseModel):
    name: str
    image_data: str
    position: Optional[str] = None

    class Config:
        orm_mode = True
