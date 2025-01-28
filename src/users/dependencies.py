from fastapi import Request, Depends
from jose import jwt, JWTError
from datetime import datetime

from config import settings
from exceptions import TokenExpiredException, TokenAbsentException, \
    IncorrectTokenException, UserIsNotPresentException, \
    AccessIsForbiddenException
from src.users.dao import UsersDAO
from src.users.models import Users


def get_token(request: Request):
    token = request.cookies.get('fluton_access_token')
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise IncorrectTokenException

    expire: str = payload.get('exp')

    if not expire or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException

    user_id = payload.get('sub')

    if not user_id:
        raise UserIsNotPresentException

    user = await UsersDAO.find_by_id(int(user_id))

    if not user:
        raise UserIsNotPresentException
    return user


async def get_current_admin_user(current_user: Users = Depends(get_current_user)):
    if current_user.privilege == 777:
        return await UsersDAO.find_all()
    raise AccessIsForbiddenException
