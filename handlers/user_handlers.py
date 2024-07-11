from Bots.ModularRockPaperScissorsBot.keyboards.keyboards import yes_no_kb, game_kb
from Bots.ModularRockPaperScissorsBot.services.services import get_bot_choice, get_winner
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from Bots.ModularRockPaperScissorsBot.lexicon.lexicon import LEXICON_RU

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)


@router.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)


@router.message(F.text == LEXICON_RU['yes_button'])
async def yes_button(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)


@router.message(F.text == LEXICON_RU['no_button'])
async def no_button(message: Message):
    await message.answer(text=LEXICON_RU['no'])


@router.message(F.text.in_([LEXICON_RU['rock'], LEXICON_RU['paper'], LEXICON_RU['scissors']]))
async def rock_paper_scissors(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)

