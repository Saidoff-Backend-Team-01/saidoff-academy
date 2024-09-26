from pydantic import BaseModel


class BannerListSchema(BaseModel):
    id: int
    title: str
    desc: str


class BannerCreateSchema(BaseModel):
    title: str
    desc: str

    class Config:
        orm_mode = True




