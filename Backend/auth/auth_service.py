from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from database import get_db
from models import RegisterModel, CurrentUser

OAuth2Scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_usernames_list(db: Session) -> list[str]:
    raise NotImplementedError("get_usernames_list is not implemented yet")


def register_user(formData: RegisterModel, db: Session):
    new_user = 


def verify_login(username: str, password: str, db: Session):
    raise NotImplementedError("verify_login is not implemented yet")


def get_current_user(
    token: str = Depends(OAuth2Scheme),
    db: Session = Depends(get_db),
) -> CurrentUser:
    raise NotImplementedError("get_current_user is not implemented yet")
