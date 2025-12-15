from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from user.model.user_model import User
from user.schema.user_schema import UserSchema, UserCreate
from user.service.user_service import get_users, get_user, get_user_by_email, get_session, create_user

user_router = APIRouter()

@user_router.get("/", response_model=list[UserSchema])
async def user_list(db: Session = Depends(get_session())):
    users = await get_users(db)
    return users


@user_router.get("/{user_id}", response_model=UserSchema)
async def get_user_by_id(db: Session = Depends(get_session()), user_id: int):
    user = await get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@user_router.post("/", response_model=UserSchema)
async def user_create(db: Session = Depends(get_session()), user: UserCreate):
    user_data = await create_user(db, user)
    return user_data


@user_create.delete("/{user_id", response_model=UserSchema)
async def user_delete(db: Session = Depends((get_session())), user_id: int):
    user = await user_delete(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user