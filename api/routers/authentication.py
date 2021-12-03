
from fastapi import APIRouter,Depends,status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security import oauth2,OAuth2PasswordRequestForm
from .. import schemas,database,models,token
from .. hashing import Hash
from sqlalchemy.orm import Session

router=APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends()
        ,db: Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND
                            ,detail='Invalid Credentails')

    if not Hash.verify(request.password,user.password):
        raise HTTPException(status.HTTP_404_NOT_FOUND
                            ,detail='Invalid Password')
    # Generate JWT
    access_token =  token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

    # return user

