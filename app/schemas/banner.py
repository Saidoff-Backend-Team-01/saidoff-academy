from pydantic import BaseModel

class BannerListSchema(BaseModel):
    id: int
    title: str
    desc: str


class Why_we_usListSchema(BaseModel):
    id: int
    title: str
    desc: str

class BannerCreateSchema(BaseModel):
    title: str
    desc: str

    class Config:
        orm_mode = True


class PortfolioCategorySchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class PortfolioItemSchema(BaseModel):
    id: int
    name: str
    category_id: int

    class Config:
        orm_mode = True

class CustomerFeedbackSchema(BaseModel):
    id: int
    customer_name: str
    feedback: str

    class Config:
        orm_mode = True
