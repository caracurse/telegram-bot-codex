from __future__ import annotations

from aiogram import Router

from app.handlers.start import router as start_router

router = Router(name=__name__)
router.include_router(start_router)
