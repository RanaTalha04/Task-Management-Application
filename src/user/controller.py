import jwt
from src.user.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from fastapi import HTTPException, status
from pwdlib import PasswordHash
from src.utils.settings import settings
from datetime import datetime, timedelta

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hash_password):
    return password_hash.verify(plain_password, hash_password)
    
def user_registration(body: UserSchema, db: Session):
    is_username = db.query(UserModel).filter(UserModel.username == body.username).first()
    
    if is_username:
        raise HTTPException(400, detail="User already Exist")   

    is_user_email = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_user_email:
        raise HTTPException(400, detail="Email already exist")
    
    is_user_mobile = db.query(UserModel).filter(UserModel.mobile_no == body.mobile_no).first()
    if is_user_mobile:
        raise HTTPException(400, detail="Mobile no already exist")
    
    hash_password = get_password_hash(body.password)

    new_user =  UserModel(
        name = body.name, 
        username = body.username,
        email = body.email,
        hash_password = hash_password, 
        mobile_no = body.mobile_no
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def user_login(body: LoginSchema, db:Session):
    username = db.query(UserModel).filter(UserModel.username == body.username).first()
    
    if not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User does not exist or name is not correct")
       
    if not verify_password(body.password, username.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User does not exist or password is not correct")
        
    
    exp_time = datetime.now() + timedelta(minutes=settings.EXP_TIME)
    
    token = jwt.encode({"_id": username.id, "exp": exp_time}, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    return {"Token": token}