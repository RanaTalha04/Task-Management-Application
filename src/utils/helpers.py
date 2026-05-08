import jwt
from fastapi import Request, status, HTTPException, Depends
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session
from src.user.models import UserModel
from src.utils.db import get_db
from src.utils.settings import settings

def is_authenticated(request: Request, db: Session = Depends(get_db)):
    
    try:
        
        token =  request.headers.get("authorization")
        if not token: 
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "Tokken not found")

        token = token.split(" ")[-1]
        
        data = jwt.decode(token, key=settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        user_id = data.get("_id")

        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "No user found")
            

        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "Tokken not found")