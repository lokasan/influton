"""Router for user"""
from fastapi import APIRouter, Response, Depends

from exceptions import UserAlreadyExistsException, \
    IncorrectEmailOrPasswordException
from src.users.dao import UsersDAO
from src.users.dependencies import get_current_user, get_current_admin_user
from src.users.models import Users
from src.users.schemas import SUserAuth, SUser
from src.utils.hash_generator import get_password_hash, authenticate_user, create_access_token

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/me')
async def get_me(user: Users = Depends(get_current_user)):
    """

    :return:
    """
    return user


@router.get('/all')
async def get_all(users: list[Users] = Depends(get_current_admin_user)):
    return users


@router.get('/{user_id}')
async def get_user(user_id: int) -> SUser:
    """

    :param user_id:
    :return:
    """
    existing_user = await UsersDAO.find_by_id(user_id)
    print(existing_user)
    return existing_user


@router.put('/{user_id}')
async def update_user(user_id: str):
    """Updated user

    :param user_id:
    :return:
    """
    return


@router.delete('/{user_id}')
async def delete_user(user_id: str):
    """Delete user by id

    :param user_id:
    :return:
    """
    return


@router.post('/register')
async def register(register_data: SUserAuth):
    """

    :param register_data:
    :return:
    """
    existing_user = await UsersDAO.find_one_or_none(email=register_data.email)
    if existing_user:
        raise UserAlreadyExistsException

    hashed_password = get_password_hash(register_data.password)

    await UsersDAO.add(first_name=register_data.first_name,
                       last_name=register_data.last_name,
                       email=register_data.email,
                       username=register_data.username,
                       hash_password=hashed_password)


@router.post('/login')
async def login(response: Response, login_data: SUserAuth):
    """

    :return:
    """
    user = await authenticate_user(email=login_data.email,
                                   password=login_data.password)
    if user is None:
        raise IncorrectEmailOrPasswordException

    access_token = create_access_token({'sub': str(user.id)})
    response.set_cookie('fluton_access_token', access_token, httponly=True)
    return access_token


@router.post('/logout')
async def logout(response: Response):
    response.delete_cookie('fluton_access_token')
    return {'is_access': True}
