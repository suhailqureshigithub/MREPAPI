from fastapi import FastAPI,Depends
from models import metadata
from database import engine,SessionLocal
import schemas
from sqlalchemy.orm import Session
import models

app=FastAPI()
# models.Base.metadata.create_all(bind=engine)
metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Post
@app.post('/blog')
def create(request: schemas.Blog ,db: Session=Depends(get_db)):
    print(db)
    new_blog=models.Blog(title='1',body='helll')
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog