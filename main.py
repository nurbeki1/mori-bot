"""
MORI IPL Consultant Bot - Main Entry Point

A Telegram bot providing information about MORI Self 10 IPL device.
Built with aiogram 3.x framework.

Usage:
    1. Set BOT_TOKEN environment variable
    2. Run: python main.py
"""

import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from bot.handlers import all_routers

# Load environment variables from .env file
load_dotenv()


def setup_logging() -> None:
    """
    Configure logging for the application.
    Sets up console handler with formatting.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    # Reduce noise from aiogram internals
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)


def get_bot_token() -> str:
    """
    Retrieve bot token from environment variables.
    Raises ValueError if token is not set.
    """
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError(
            "BOT_TOKEN environment variable is not set. "
            "Please set it before running the bot.\n"
            "Example: export BOT_TOKEN='your_token_here'"
        )

    return token


async def on_startup(bot: Bot) -> None:
    """
    Called when bot starts.
    Can be used for initialization tasks.
    """
    bot_info = await bot.get_me()
    logging.info(f"Bot started: @{bot_info.username}")


async def on_shutdown(bot: Bot) -> None:
    """
    Called when bot shuts down.
    Performs cleanup tasks.
    """
    logging.info("Bot is shutting down...")
    await bot.session.close()


async def main() -> None:
    """
    Main function to run the bot.
    Initializes bot, dispatcher, registers handlers and starts polling.
    """
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)

    # Get bot token
    try:
        token = get_bot_token()
    except ValueError as e:
        logger.error(str(e))
        sys.exit(1)

    # Initialize bot with default HTML parse mode
    bot = Bot(
        token=token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    # Initialize dispatcher
    dp = Dispatcher()

    # Register startup and shutdown handlers
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    # Register all routers
    for router in all_routers:
        dp.include_router(router)
        logger.info(f"Registered router: {router.name}")

    logger.info("Starting bot polling...")

    try:
        # Start polling (long-polling mode)
        await dp.start_polling(
            bot,
            allowed_updates=dp.resolve_used_update_types(),
            close_bot_session=False
        )
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped by user")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        sys.exit(1)
