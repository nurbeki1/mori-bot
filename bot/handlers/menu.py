"""
Menu handlers for MORI IPL Consultant Bot.
Contains command and callback handlers for all bot sections.
"""

import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode

from bot.keyboards.inline import (
    get_main_menu_keyboard,
    get_back_button_keyboard,
    get_video_keyboard,
    CallbackData,
)
from bot.texts.content import (
    WELCOME_TEXT,
    SCHEME_TEXT,
    INSTRUCTION_TEXT,
    REJUVENATION_TEXT,
    COURSE_TEXT,
    SKIN_REACTION_TEXT,
    SAFETY_TEXT,
    FAQ_TEXT,
    VIDEO_TEXT,
)

# Initialize router for menu handlers
router = Router(name="menu")

# Logger for this module
logger = logging.getLogger(__name__)


# ==================== Command Handlers ====================

@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """
    Handle /start command.
    Shows welcome message with main menu keyboard.
    """
    logger.info(f"User {message.from_user.id} started the bot")

    await message.answer(
        text=WELCOME_TEXT,
        reply_markup=get_main_menu_keyboard(),
        parse_mode=ParseMode.HTML
    )


# ==================== Callback Handlers ====================

@router.callback_query(F.data == CallbackData.BACK_TO_MENU)
async def callback_back_to_menu(callback: CallbackQuery) -> None:
    """
    Handle back to menu button.
    Returns user to main menu.
    """
    logger.debug(f"User {callback.from_user.id} returned to main menu")

    await callback.message.edit_text(
        text=WELCOME_TEXT,
        reply_markup=get_main_menu_keyboard(),
        parse_mode=ParseMode.HTML
    )
    await callback.answer()


@router.callback_query(F.data == CallbackData.SCHEME)
async def callback_scheme(callback: CallbackQuery) -> None:
    """Handle 'Схема применения' section."""
    logger.debug(f"User {callback.from_user.id} opened scheme section")

    await callback.message.edit_text(
        text=SCHEME_TEXT,
        reply_markup=get_back_button_keyboard(),
        parse_mode=ParseMode.HTML
    )
    await callback.answer()


@router.callback_query(F.data == CallbackData.INSTRUCTION)
async def callback_instruction(callback: CallbackQuery) -> None:
    """Handle 'Подробная инструкция' section."""
    logger.debug(f"User {callback.from_user.id} opened instruction section")

    await callback.message.edit_text(
        text=INSTRUCTION_TEXT,
        reply_markup=get_back_button_keyboard(),
        parse_mode=ParseMode.HTML
    )
    await callback.answer()


@router.callback_query(F.data == CallbackData.REJUVENATION)
async def callback_rejuvenation(callback: CallbackQuery) -> None:
    """Handle 'Омоложение и насадки' section."""
    logger.debug(f"User {callback.from_user.id} opened rejuvenation section")

    await callback.message.edit_text(
        text=REJUVENATION_TEXT,
        reply_markup=get_back_button_keyboard(),
        parse_mode=ParseMode.HTML
    )
    await callback.answer()


@router.callback_query(F.data == CallbackData.COURSE)
async def callback_course(callback: CallbackQuery) -> None:
    """Handle 'Почему нужен курс' section."""
    logger.debug(f"User {callback.from_user.id} opened course section")

    await callback.message.edit_text(
        text=COURSE_TEXT,
        reply_markup=get_back_button_keyboard(),
        parse_mode=ParseMode.HTML
    )
    await callback.answer()


@router.callback_query(F.data == CallbackData.SKIN_REACTION)
async def callback_skin_reaction(callback: CallbackQuery) -> None:
    """Handle 'Нормальная реакция кожи' section."""
    logger.debug(f"User {callback.from_user.id} opened skin reaction section")

    await callback.message.edit_text(
        text=SKIN_REACTION_TEXT,
        reply_markup=get_back_button_keyboard(),
        parse_mode=ParseMode.HTML
    )
    await callback.answer()


@router.callback_query(F.data == CallbackData.SAFETY)
async def callback_safety(callback: CallbackQuery) -> None:
    """Handle 'Безопасность' section."""
    logger.debug(f"User {callback.from_user.id} opened safety section")

    await callback.message.edit_text(
        text=SAFETY_TEXT,
        reply_markup=get_back_button_keyboard(),
        parse_mode=ParseMode.HTML
    )
    await callback.answer()


@router.callback_query(F.data == CallbackData.FAQ)
async def callback_faq(callback: CallbackQuery) -> None:
    """Handle 'Частые вопросы' section."""
    logger.debug(f"User {callback.from_user.id} opened FAQ section")

    await callback.message.edit_text(
        text=FAQ_TEXT,
        reply_markup=get_back_button_keyboard(),
        parse_mode=ParseMode.HTML
    )
    await callback.answer()


@router.callback_query(F.data == CallbackData.VIDEO)
async def callback_video(callback: CallbackQuery) -> None:
    """Handle 'Видеоинструкция' section with video link."""
    logger.debug(f"User {callback.from_user.id} opened video section")

    await callback.message.edit_text(
        text=VIDEO_TEXT,
        reply_markup=get_video_keyboard(),
        parse_mode=ParseMode.HTML
    )
    await callback.answer()
