import email
from pydantic import BaseModel
from typing import List, Optional
from typing import Union
from database import Base

class Todo(BaseModel):
    title : str
    body : Optional[str]=None


class User(BaseModel):
    name : str
    email : str
    password : str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs : List[User] =[]
    class Config():
        orm_mode = True


class Login(BaseModel):
    email : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None