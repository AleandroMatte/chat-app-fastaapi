from typing import Annotated

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jwt.exceptions import InvalidTokenError

from src.domain.users.dto.token_dto import UserTokenData
from src.domain.users.dto.user_dtos import SharedUserDto
from src.domain.users.repositories.user_repository import UserRepository
from src.providers.token_provider import TokenProvider


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
token_provier = TokenProvider()
user_repository = UserRepository()


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = await token_provier.get_decoded_token(token)
        username = payload.get("username")
        if username is None:
            raise credentials_error
        token_data = UserTokenData.model_validate(payload)
    except InvalidTokenError:
        raise credentials_error
    user = user_repository.get_by_id(token_data.id)
    if user is None:
        raise credentials_error
    return SharedUserDto.model_validate(user, from_attributes=True)
