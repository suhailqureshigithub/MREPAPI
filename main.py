from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

@app.get('/blog')
def index(limit=100,published:bool =True,sort:Optional[str]=None):

    if published:
        return{'data': f'{limit} published blog(s) from DB'}
    else:
        return{'data': f'All blog(s) from DB'}


@app.get('/blog/unpublished')
def unpublished():
    return{'List of all unpublished blog':'All'}

@app.get('/blog/{id}')
def show(id:int):
    return{'blog id':id}

@app.get('/blog/{id}/comments')
def show(id:int):
    return{'blog id with comments':{'1','2'}}

#Post Method
class Blog(BaseModel):


@app.post('/blog')
def create_blog():
    return{'Blog Post':'Blog created'}
