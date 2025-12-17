from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.auth.service.auth_service import create_access_token, authenticate_user
from app.auth.model.auth_model import Token, SignUpData, SignINData
from app.user.service.user_service import create_user
from app.user.model.user_model import User
from typing import Annotated
from app.core.db import get_session
from datetime import timedelta

from app.user.schema.user_schema import UserSchema

auth_router = APIRouter()

@auth_router.post("/token", response_model=Token)
async def login_for_access_token(
        from_data: Annotated[OAuth2PasswordRequestForm,
        Depends()], db: Session = Depends(get_session)
    ) -> Token:
    user = authenticate_user(db, from_data.username, from_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=1440)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@auth_router.post("/signup", response_model=SignUpData)
async def signup(from_data: SignUpData, db: Session = Depends(get_session)) -> SignUpData:
    user = create_user(db, from_data)
    return user

@auth_router.post("/login", response_model=Token)
async def login(form_data: SignINData, db: Session = Depends(get_session)) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username},
    )
    return Token(access_token=access_token, token_type="bearer")