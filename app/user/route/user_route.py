from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.service.auth_service import get_current_active_user
from app.user.model.user_model import User
from app.user.schema.user_schema import UserSchema, UserCreate
from app.user.service.user_service import get_users, get_user, create_user
from app.core.db import get_session

user_router = APIRouter()

@user_router.get("/", response_model=list[UserSchema])
async def user_list(db: Session = Depends(get_session())):
    users = await get_users(db)
    return users


@user_router.get("/{user_id}", response_model=UserSchema)
async def get_user_by_id(db: Session = Depends(get_session()), user_id: int = None):
    user = await get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@user_router.post("/", response_model=UserSchema)
async def user_create(db: Session = Depends(get_session()), user: UserCreate = None):
    user_data = await create_user(db, user)
    return user_data


@user_create.delete("/{user_id}", response_model=UserSchema)
async def user_delete(db: Session = Depends((get_session())), user_id: int = None):
    user = await user_delete(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.get("/me", response_model=UserSchema)
def get_current_active_user(current_user: User = Depends(get_current_active_user)):
    return current_user