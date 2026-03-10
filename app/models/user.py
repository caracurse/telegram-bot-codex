from __future__ import annotations

from datetime import datetime

from sqlalchemy import BigInteger, Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base, TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str | None] = mapped_column(String(64), nullable=True, index=True)
    gold: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    energy: Mapped[int] = mapped_column(Integer, default=100, nullable=False)
    exp: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    level: Mapped[int] = mapped_column(Integer, default=1, nullable=False, index=True)
    is_blocked: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, index=True)
    last_daily_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
