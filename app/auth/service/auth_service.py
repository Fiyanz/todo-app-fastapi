import jwt
from jwt.exceptions import InvalidTokenError
from app.core.config import settings
from app.core.db import get_session
from app.auth.model.auth_model import TokerData, SignUpData, SignINData
from app.auth.uttil.pass_hash import verify_pass, pass_hash
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from app.user.model.user_model import User
from app.user.schema.user_schema import UserCreate
from app.user.service.user_service import get_user_by_email, get_user_by_username
from typing import Annotated


SECRET_CODE = settings.JWT_TOKEN
ALGORITHM = settings.ALGORITHM

oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/token")

def authenticate_user(db: Session = Depends(get_session), username_user: str = None, password: str = None):
    user = get_user_by_username(db, username_user)
    if not user: return None
    if not verify_pass(password, user.password):
        return None
    return None


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encode_jwt_token = jwt.encode(to_encode, SECRET_CODE, algorithm=ALGORITHM)
    return encode_jwt_token

async def get_current_user(token: Annotated[str, Depends(oauth2)], db: Session = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        pyload = jwt.decode(token, SECRET_CODE, algorithms=ALGORITHM)
        username = pyload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokerData(username=username)
    except InvalidTokenError:
        raise credentials_exception

    user = get_user_by_username(db, token_data.username)
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user
