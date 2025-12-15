from pydantic import BaseModel
from pydantic_core.core_schema import none_schema


class Token(BaseModel):
    access_token: str
    token_type: str

class TokerData(BaseModel):
    email: str | None = None

