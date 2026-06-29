from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import get_db
from models import RegisterModel, CurrentUser
from auth import auth_service

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/login")
def login(
    formData: OAuth2PasswordRequestForm = Depends(),  # For Swagger Docs
    db: Session = Depends(get_db),
):
    return auth_service.verify_login(formData.username, formData.password, db)


@auth_router.post("/register")
def register(formData: RegisterModel, db: Session = Depends(get_db)):
    return auth_service.register_user(formData, db)


@auth_router.get("/me")
def me(user: CurrentUser = Depends(auth_service.get_current_user)):
    return user


@auth_router.get("/get-users")
def get_users(db: Session = Depends(get_db)):
    return auth_service.get_usernames_list(db)
