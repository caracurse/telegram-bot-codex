from __future__ import annotations

from typing import Any

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str = Field(alias="BOT_TOKEN")
    postgres_dsn: str = Field(alias="POSTGRES_DSN")
    redis_dsn: str = Field(alias="REDIS_DSN")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    admin_ids: tuple[int, ...] = Field(default=(), alias="ADMIN_IDS")

    @field_validator("admin_ids", mode="before")
    @classmethod
    def parse_admin_ids(cls, value: Any) -> Any:
        if isinstance(value, str):
            raw = [item.strip() for item in value.split(",") if item.strip()]
            return tuple(int(item) for item in raw)
        return value

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
