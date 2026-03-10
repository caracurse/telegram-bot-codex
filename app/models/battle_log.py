from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base, TimestampMixin


class BattleLog(Base, TimestampMixin):
    __tablename__ = "battle_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    mob_code: Mapped[str] = mapped_column(String(64), nullable=False)
    result: Mapped[str] = mapped_column(String(16), nullable=False, index=True)
    turns: Mapped[int] = mapped_column(Integer, nullable=False)
    reward_gold: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    reward_exp: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    details: Mapped[str] = mapped_column(Text, default="", nullable=False)
