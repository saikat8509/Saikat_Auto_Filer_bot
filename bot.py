import asyncio
from pyrogram import Client, filters
from bot.config import BOT_TOKEN, API_ID, API_HASH
from bot.handlers import (start, filters_handler, admin, stats, broadcast,
                          subscription, premium, referral, verify_handler)
from bot.utils.logger import LOGGER


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="AutoFilterBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "bot.handlers"}
        )

    async def start_bot(self):
        await self.start()
        me = await self.get_me()
        LOGGER.info(f"Bot Started as {me.first_name} (@{me.username})")

    async def stop_bot(self):
        await self.stop()
        LOGGER.info("Bot stopped successfully.")


async def main():
    bot = Bot()
    await bot.start_bot()
    await idle()
    await bot.stop_bot()


if __name__ == "__main__":
    from pyrogram import idle
    asyncio.run(main())
