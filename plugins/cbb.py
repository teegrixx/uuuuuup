#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>TEEGRIXX</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/grixxtech'>GRIXXTECH</a>\n○ 18+ : <a href='https://t.me/upcomicc'>MANHWA</a>\n○ MANHWA : <a href='https://t.me/Manhwa_clubb'>MANHWA CLUB</a>\n○ ANIME CLUBB : <a hrefhttps://t.me/Anime_clubb_ac '>LATEST ANIMES</a>/n○ MANHWA CLOUD : <a href='https://t.me/manhwa_Clouud'>CLOUD ☁️</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("ClOze", callback_data = "close"),
                    InlineKeyboardButton('MY HOME', url='https://t.me/Anime_Nation')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
