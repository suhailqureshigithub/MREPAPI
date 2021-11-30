from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import false

SQLALCHEMY_DATABASE_URL='sqlite:///./blog.db'

engine=create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal=sessionmaker(bind=engine,autocommit=false,autoflush=false)
Base=declarative_base()



