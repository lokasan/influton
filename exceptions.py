from fastapi import HTTPException, status

UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="User already exists",
    headers={"X-Error": "User already exists"}, )

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Invalid password or email', )

TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Token expired',
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Token absent',
)

IncorrectTokenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Incorrect token',
)

UserIsNotPresentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
)

AccessIsForbiddenException = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail='Access is forbidden',
)
