from fastapi import APIRouter, Depends
import schemas,models,database
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import status , Response, HTTPException
from routers import oauth2

router = APIRouter(
    tags=['Todo_list']
)


@router.get('/todo',)
def all(db: Session=Depends(database.get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    todo = db.query(models.Todo).all()
    return todo

@router.get('/todo/{id}',status_code=200,)
def show (id : int,response:Response,db: Session=Depends(database.get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail =f'todo id={id} result not found ')
    return todo

@router.post('/todo', status_code = status.HTTP_201_CREATED, )
def create_todo(request : schemas.Todo , db: Session=Depends(database.get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    new_todo = models.Todo(title = request.title, body = request.body)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo 

@router.put('/todo/{id}',status_code=status.HTTP_200_OK, )
def update(request : schemas.Todo ,id: int,db: Session=Depends(database.get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    todo = db.query(models.Todo).filter(models.Todo.id == id)
    if not todo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail =f'todo id={id} result not found ')
    todo.update({'title':request.title,'body':request.body})
    db.commit()
    return {'detail': f' updated the value of id {id}'}


@router.delete('/todo/{id}', status_code = status.HTTP_204_NO_CONTENT,)
def destory(id: int,db: Session=Depends(database.get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    todo = db.query(models.Todo).filter(models.Todo.id == id)
    if not todo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail =f'todo id={id} result not found ')
    todo.delete(synchronize_session=False)
    db.commit()
    return {'detail': 'done'}