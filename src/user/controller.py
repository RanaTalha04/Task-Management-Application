from src.user.dtos import UserSchema
from sqlalchemy.orm import Session


def user_registration(body: UserSchema, db: Session):
    print(body)
    return {
        "status": "Registration Done"
    }