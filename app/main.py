from __future__ import annotations

import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from app.config.logging import configure_logging
from app.config.settings import Settings
from app.database.session import create_engine, create_session_factory
from app.handlers.router import router
from app.middlewares.db_session import DbSessionMiddleware
from app.middlewares.service_container import ServiceContainerMiddleware


async def main() -> None:
    settings = Settings()
    configure_logging(settings.log_level)

    redis = Redis.from_url(settings.redis_dsn, decode_responses=True)
    storage = RedisStorage(redis=redis)

    engine = create_engine(settings)
    session_factory = create_session_factory(engine)

    bot = Bot(token=settings.bot_token)
    dp = Dispatcher(storage=storage)

    dp.update.middleware(DbSessionMiddleware(session_factory=session_factory))
    dp.update.middleware(ServiceContainerMiddleware())
    dp.include_router(router)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await redis.aclose()
        await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
