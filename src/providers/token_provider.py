from datetime import datetime, timedelta
import os
from fastapi import HTTPException
import jwt


class TokenProvider:
    def __init__(self) -> None:
        self._algorithm = os.environ.get("ALGORITHM")
        self.__expire = 30

    async def _get_secret_key(self):
        # secret_key = os.environ.get("SECRET_KEY")
        return os.environ.get("TOKEN_KEY_SECRET_KEY")

    async def _decode_token(self, token: str):
        try:
            decoded_token = jwt.decode(
                token,
                await self._get_secret_key(),
                algorithms=[self._algorithm],
            )
            return decoded_token
        except jwt.InvalidTokenError as e:
            raise HTTPException("Token is expired or not valid") from e

    async def create_token(self, data: dict, expiration_in_minutes: int = 60) -> str:
        expire = datetime.now() + timedelta(minutes=expiration_in_minutes)
        expire_timestamp = expire.timestamp()
        data.update({"exp": int(expire_timestamp)})
        encoded_jwt = jwt.encode(
            data,
            await self._get_secret_key(),
            algorithm=os.environ.get("ALGORITHM", None),
        )
        return encoded_jwt

    def get_expire_date(self) -> int:
        return self.__expire

    async def get_decoded_token(self, token: str):
        return await self._decode_token(token)
