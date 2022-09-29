from unicodedata import name
from database import Base
from sqlalchemy import Column , Integer, String


class Todo(Base):
    __tablename__='todo_list'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)


class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
