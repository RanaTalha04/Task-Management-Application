from fastapi import APIRouter, Depends, status
from src.user import controller
from src.utils.db import get_db
from src.user.dtos import UserSchema
from sqlalchemy.orm import Session

user_routes = APIRouter(prefix="/user")


@user_routes.post("/register", status_code=status.HTTP_201_CREATED)
def user_registeration(body: UserSchema, db: Session = Depends(get_db)):
    return controller.user_registration(body, db )
