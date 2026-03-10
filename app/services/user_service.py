from __future__ import annotations

from app.models import User
from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    async def register(self, *, user_id: int, username: str | None) -> User:
        user = await self._user_repository.get_by_id(user_id)
        if user is not None:
            return user
        return await self._user_repository.create(user_id=user_id, username=username)
