import asyncio, os
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from StringSessionBot.database.mongo import semua, hapus

@Client.on_message(filters.command('users') & filters.private & filters.user(1814359323))
async def get_users(Client, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text="Tunggu sebentar...")
    users = await semua()
    await msg.edit(f"{len(users)} users are using this bot")

@Client.on_message(filters.private & filters.command('broadcast') & filters.user(1814359323))
async def send_text(Client, message: Message):
    if message.reply_to_message:
        query = await semua()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await hapus(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await hapus(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b><u>Broadcast Completed</u>

Total Users: <code>{total}</code>
Successful: <code>{successful}</code>
Blocked Users: <code>{blocked}</code>
Deleted Accounts: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code></b>"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply("reply babi...")
        await asyncio.sleep(8)
        await msg.delete()
