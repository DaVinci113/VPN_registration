from aiogram.filters import CommandStart
from handlers import dp, Message


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """

