from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    full_name: str | None = None

class UserCreate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None

class UserSchema(BaseModel):
    id: int

    class Config:
        from_atributes = True
        orm_mode = True