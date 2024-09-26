from pydantic import BaseModel


class ConfigModel(BaseModel):
    id: int
    phone: str
    email: str