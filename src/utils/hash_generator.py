from datetime import datetime, timedelta

from passlib.context import CryptContext
from jose import jwt
from pydantic import EmailStr

from config import settings
from src.users.dao import UsersDAO

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str) -> str:
    """"""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """"""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY,
                             algorithm=settings.ALGORITHM)
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    """"""
    user = await UsersDAO.find_one_or_none(email=email)

    if user and verify_password(password,
                                user.hash_password):
        return user
