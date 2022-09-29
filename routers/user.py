from fastapi import APIRouter, Depends
import schemas,models,database, hashing
from sqlalchemy.orm import Session
from fastapi import status 

router = APIRouter(
    tags=['User']
    )


@router.post('/user')
def create_user(request: schemas.User, db: Session=Depends(database.get_db)):
    new_user = models.User(name=request.name,email=request.email,password=hashing.Hash.bycrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
