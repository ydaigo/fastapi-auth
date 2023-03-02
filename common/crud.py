from passlib.context import CryptContext
from sqlalchemy.orm import Session

from common import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db: Session, user_id: str):
    """ユーザ取得"""
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """メールに紐づくユーザ取得"""
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_username(db: Session, username: str):
    """ユーザ名に紐づくユーザ取得"""
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: get_user = 0, limit: get_user = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, username=user.username, hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
