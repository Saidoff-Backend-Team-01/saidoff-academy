from pydantic import BaseModel
from typing import Optional


class FaqListSchemas(BaseModel):
    id: int
    question: str
    answer: str
    faq_type: str


class FaqCreateSchemas(BaseModel):
    question: str
    answer: str
    faq_type: Optional[str] = None

    class Config:
        orm_mode = True

