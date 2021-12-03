
from fastapi import APIRouter,Depends,HTTPException,status,Response
from .. import schemas,models,database,oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import repBlog

router=APIRouter(
    prefix='/blog',
    tags=['blogs']
)

# Post
@router.post('/',status_code=status.HTTP_201_CREATED )
def createBlog(request: schemas.Blog ,db: Session=Depends(database.get_db)
            ,get_current_user: schemas.User=Depends(oauth2.get_current_user)
            ):
    return repBlog.createBlog(db,request)

# Get
@router.get('/',response_model=List[schemas.showBlog] )
def allBlog(db: Session=Depends(database.get_db)
            ,get_current_user: schemas.User=Depends(oauth2.get_current_user)  ):
    return repBlog.get_all(db)

@router.get(
    '/{id}', status_code=status.HTTP_302_FOUND,response_model=schemas.showBlog)
def findBlog(id:int, db: Session=Depends(database.get_db)
                ,get_current_user: schemas.User=Depends(oauth2.get_current_user)
            ):
    return repBlog.get_byId(db,id)

# Delete
@router.delete('/',status_code=status.HTTP_204_NO_CONTENT )
def deleteBlog(id:int, db: Session=Depends(database.get_db)
                ,get_current_user: schemas.User=Depends(oauth2.get_current_user)
            ):
    return repBlog.del_blog(db,id)

#Update
@router.put('/',status_code=status.HTTP_202_ACCEPTED )
def blogUpdate(id:int,request: schemas.Blog,  db: Session=Depends(database.get_db)
                ,get_current_user: schemas.User=Depends(oauth2.get_current_user)
            ):
    return repBlog.upd_blog(db,id,request)