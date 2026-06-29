from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column,Integer,String,Boolean
from database import Base


class RegisterModel(BaseModel):
    username: str
    password: str
    confirmPassword: str


class CurrentUser(BaseModel):
    id: str
    username: str

class UserModel(Base):
    __tablename__="users"
    id = Column(String,primary_key=True,default=lambda:str.uuid())
    username = Column(String)
    password = Column(String)