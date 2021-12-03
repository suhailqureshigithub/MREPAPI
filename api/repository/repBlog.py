
from pydantic.errors import SetError
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from..  import models,schemas

def get_all(db: Session):
    blogList=db.query(models.Blog).all()
    return blogList

def get_byId(db: Session,id):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND
                            ,detail=f'Blog not found with Blog {id}')
    return blog

def del_blog(db: Session,id):
    deleteBlog=db.query(models.Blog).filter(models.Blog.id==id)
    if not deleteBlog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail='Not found')

    deleteBlog.delete(synchronize_session=False)
    db.commit()
    return 'Blog Deleted'

def upd_blog(db:Session,id,request):
    blogUpdate=db.query(models.Blog).filter(models.Blog.id==id)
    if not blogUpdate.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail='No Blog Found')
    blogUpdate.update(request.dict())
    db.commit()
    return 'Blog Updated'

def createBlog(db: Session,request: schemas.Blog):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

