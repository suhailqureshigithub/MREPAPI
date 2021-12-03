from fastapi import APIRouter,Depends,HTTPException,status,Response
# from fastapi import FastAPI,Depends,status,Response,HTTPException
from.. import schemas,models,database,oauth2
from typing import List
from sqlalchemy.orm import Session
from.. hashing import Hash
from ..repository import repUser

router=APIRouter(
    prefix='/user',
    tags=['users']
)

#Post
@router.post('/',status_code=status.HTTP_201_CREATED
            ,response_model=schemas.showUser  )
def create(request: schemas.User ,db: Session=Depends(database.get_db)):
    return repUser.createUser(db,request)

#Get Users
@router.get('/{id}',response_model=schemas.showUser)
def findUser(id:int, db: Session=Depends(database.get_db)):
    return repUser.getUserById(db,id)

@router.get('/',response_model=List[schemas.showUser])
def getAllUsers(db: Session=Depends(database.get_db)
                ,get_current_user: schemas.User=Depends(oauth2.get_current_user)
                ):
    return repUser.getAllUsers(db)
