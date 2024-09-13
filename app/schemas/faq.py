from pydantic import BaseModel
from typing import Optional, List


class FaqListSchemas(BaseModel):
    id: int
    question: str
    answer: str
    faq_type: str


class FaqCreateSchemas(BaseModel):
    id: int
    question: str
    answer: str
    faq_type: Optional[str] = None

    class Config:
        orm_mode = True

