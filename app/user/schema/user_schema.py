from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    full_name: str | None = None

class UserCreate(UserBase):
    password: str

class UserSchema(UserBase):
    id: int

    class Config:
        from_atributes = True