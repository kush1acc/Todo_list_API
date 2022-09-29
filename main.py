
from fastapi import FastAPI 

import  models 
from database import engine
from routers import todo,user,aunthecation


app = FastAPI()
app.include_router(aunthecation.router)
app.include_router(user.router)
app.include_router(todo.router)
models.Base.metadata.create_all(engine)



