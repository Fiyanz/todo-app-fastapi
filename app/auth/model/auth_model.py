from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class RequestToken(BaseModel):
    refresh_token: str

class RefreshToken(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
    username: str | None = None

class SignUpData(BaseModel):
    email: str | None = None
    username: str | None = None
    password: str | None = None

class SignINData(BaseModel):
    username: str | None = None
    password: str | None = None
