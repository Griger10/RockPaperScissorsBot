from aiogram import Router
from aiogram.types import Message
from Bots.ModularRockPaperScissorsBot.lexicon.lexicon import LEXICON_RU


router = Router()


@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])
