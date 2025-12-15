from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str

class TokerData(BaseModel):
    email: str | None = None
    username: str | None = None

