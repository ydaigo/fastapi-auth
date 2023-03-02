from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.auth_api import get_current_active_user
from api.dps import get_db
from common import schemas, crud
from common.models import User

router = APIRouter()


@router.get("/users/me", response_model=schemas.User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")
    return crud.create_user(db=db, user=user)
