from __future__ import annotations

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def build_main_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="👤 Profile"), KeyboardButton(text="🎮 Play")],
            [KeyboardButton(text="🛒 Shop"), KeyboardButton(text="🎒 Inventory")],
            [KeyboardButton(text="📜 Quests"), KeyboardButton(text="🏆 Leaderboard")],
        ],
        resize_keyboard=True,
    )
