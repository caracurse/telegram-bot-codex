from __future__ import annotations

from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base, TimestampMixin


class Quest(Base, TimestampMixin):
    __tablename__ = "quests"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(64), unique=True, nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    quest_type: Mapped[str] = mapped_column(String(32), nullable=False, index=True)
    target_value: Mapped[int] = mapped_column(Integer, nullable=False)
    reward_gold: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    reward_exp: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
