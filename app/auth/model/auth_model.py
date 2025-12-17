from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str

class TokerData(BaseModel):
    email: str | None = None
    username: str | None = None

class SignUpData(BaseModel):
    email: str | None = None
    username: str | None = None
    password: str | None = None

class SignINData(BaseModel):
    username: str | None = None
    password: str | None = None
