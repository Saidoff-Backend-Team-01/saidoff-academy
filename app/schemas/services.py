from pydantic import BaseModel


class ServicesListSchema(BaseModel):
    id: int
    title: str
    desc: str
    slug: str


class ServicesCreateSchema(BaseModel):
    title: str
    desc: str
    slug: str

    class Config:
        orm_mode = True

