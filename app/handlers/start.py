from __future__ import annotations

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards.main_menu import build_main_menu
from app.services.user_service import UserService

router = Router(name=__name__)


@router.message(CommandStart())
async def start_handler(message: Message, user_service: UserService) -> None:
    if message.from_user is None:
        return

    user = await user_service.register(
        user_id=message.from_user.id,
        username=message.from_user.username,
    )

    await message.answer(
        text=(
            "Welcome to RPG bot!\n"
            f"Profile created: id={user.id}, level={user.level}, gold={user.gold}, energy={user.energy}"
        ),
        reply_markup=build_main_menu(),
    )
