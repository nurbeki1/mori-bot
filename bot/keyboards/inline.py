"""
Inline keyboards for MORI IPL Consultant Bot.
Contains all keyboard layouts and button configurations.
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.texts.content import VIDEO_URL


# Callback data constants for better maintainability
class CallbackData:
    """Constants for callback data to avoid typos and enable refactoring."""
    SCHEME = "scheme"
    INSTRUCTION = "instruction"
    REJUVENATION = "rejuvenation"
    COURSE = "course"
    SKIN_REACTION = "skin_reaction"
    SAFETY = "safety"
    FAQ = "faq"
    VIDEO = "video"
    BACK_TO_MENU = "back_to_menu"


def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    """
    Creates the main menu keyboard with all section buttons.
    Returns InlineKeyboardMarkup with 8 section buttons arranged in 2 columns.
    """
    builder = InlineKeyboardBuilder()

    # Define menu buttons with their callback data
    buttons = [
        ("Схема применения", CallbackData.SCHEME),
        ("Подробная инструкция", CallbackData.INSTRUCTION),
        ("Омоложение и насадки", CallbackData.REJUVENATION),
        ("Почему нужен курс", CallbackData.COURSE),
        ("Нормальная реакция кожи", CallbackData.SKIN_REACTION),
        ("Безопасность", CallbackData.SAFETY),
        ("Частые вопросы", CallbackData.FAQ),
        ("Видеоинструкция", CallbackData.VIDEO),
    ]

    # Add buttons to builder
    for text, callback_data in buttons:
        builder.button(text=text, callback_data=callback_data)

    # Arrange in 1 column for better readability
    builder.adjust(1)

    return builder.as_markup()


def get_back_button_keyboard() -> InlineKeyboardMarkup:
    """
    Creates a simple back button keyboard.
    Returns InlineKeyboardMarkup with single back button.
    """
    builder = InlineKeyboardBuilder()
    builder.button(
        text="🔙 Назад в главное меню",
        callback_data=CallbackData.BACK_TO_MENU
    )
    return builder.as_markup()


def get_video_keyboard() -> InlineKeyboardMarkup:
    """
    Creates keyboard for video section with video link and back button.
    Returns InlineKeyboardMarkup with video URL button and back button.
    """
    builder = InlineKeyboardBuilder()

    # Video link button (opens in browser)
    builder.button(
        text="▶ Смотреть видео",
        url=VIDEO_URL
    )

    # Back to menu button
    builder.button(
        text="🔙 Назад в главное меню",
        callback_data=CallbackData.BACK_TO_MENU
    )

    # Arrange buttons vertically
    builder.adjust(1)

    return builder.as_markup()
