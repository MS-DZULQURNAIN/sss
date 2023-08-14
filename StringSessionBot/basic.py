from data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message
from StringSessionBot.database.mongo import cek, tambah, semua, user_data

def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)


# Start Message
@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    id = await msg.from_user.id
    if not await cek(id):
        try:
            await tambah(id)
        except:
            pass
    user = await bot.get_me()
    mention = user.mention
    pengguna = user_data.count_document({})  #await semua({}) 
    await bot.send_message(
        msg.chat.id,
        Data.START.format(msg.from_user.mention, mention, pengguna),
        reply_markup=InlineKeyboardMarkup(Data.buttons)
    )


# Help Message
@Client.on_message(filter("help"))
async def _help(bot: Client, msg: Message):
    await bot.send_message(
        msg.chat.id, Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )


# About Message
@Client.on_message(filter("about"))
async def about(bot: Client, msg: Message):
    await bot.send_message(
        msg.chat.id,
        Data.ABOUT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
    )
