from typing import List,Optional
from pydantic import BaseModel
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import Integer

class Blog(BaseModel):
    title:str
    body:str
    user_id:int

    class Config():
        orm_mode=True

class BlogList(BaseModel):
    title:str
    body:str

    class Config():
        orm_mode=True


class User(BaseModel):
    name:str
    email:str
    password:str

class UserDetails(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode=True


class showUser(BaseModel):
    name:str
    email:str
    # blogs is relationship name used in models
    blogs: List[BlogList]

    class Config():
        orm_mode=True

class showBlog(BaseModel):
    title:str
    body:str
    creator:UserDetails

    class Config():
        orm_mode=True

class Login(BaseModel):
    userEmail:str
    password:str

    class Config():
        orm_mode=True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
