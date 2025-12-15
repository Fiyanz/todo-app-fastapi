from sqlalchemy.orm import Session

from app.auth.uttil.pass_hash import pass_hash
from app.user.model.user_model import User
from app.user.schema.user_schema import UserCreate



def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, user_email: str):
    return db.query(User).filter(User.email == user_email).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        password=pass_hash(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return
