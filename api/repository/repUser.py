
from pydantic.errors import SetError
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from.. hashing import Hash
from..  import models,schemas

def createUser(db: Session, request: schemas.User):
    newUser=models.User(name=request.name,email=request.email
                    ,password=Hash.bcrypt(request.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

def getUserById(db: Session ,id):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND
                            ,detail=f'User not found with UserId {id}')
    return user

def getAllUsers(db: Session):
    user=db.query(models.User).all()
    return user