from fastapi import APIRouter, Depends
import schemas,models,database
from sqlalchemy.orm import Session
from fastapi import status , Response, HTTPException
from hashing import Hash
from jose import JWTError, jwt
from routers import token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Login']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends() , db: Session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail ='user not found ')
    if not Hash.verify(user.password ,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail ='invalid credantials ')
    
    
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
    
