from os import name
from fastapi import FastAPI,Depends,status,Response,HTTPException

# from sqlalchemy.orm import Session
from .models import metadata
from . database import engine
from . import models,schemas,database
from fastapi import FastAPI
from.routers import blog,user,authentication

app=FastAPI()
models.Base.metadata.create_all(bind=engine)

#Including Routers
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

