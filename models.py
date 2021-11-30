from sqlalchemy.sql.schema import MetaData
from database import Base,SessionLocal
from sqlalchemy import Column,Integer,String


metadata=MetaData()

class Blog(Base):
    __tablename__ ='blogs'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)






