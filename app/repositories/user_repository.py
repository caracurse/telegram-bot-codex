from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, user_id: int) -> User | None:
        return await self._session.get(User, user_id)

    async def create(self, *, user_id: int, username: str | None) -> User:
        user = User(id=user_id, username=username)
        self._session.add(user)
        await self._session.flush()
        return user

    async def top_by_level(self, limit: int = 10) -> list[User]:
        query = select(User).order_by(User.level.desc(), User.exp.desc()).limit(limit)
        result = await self._session.scalars(query)
        return list(result)
