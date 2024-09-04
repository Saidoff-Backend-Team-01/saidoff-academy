from pydantic import BaseModel


class Why_we_usListSchema(BaseModel):
    id: int
    title: str
    desc: str