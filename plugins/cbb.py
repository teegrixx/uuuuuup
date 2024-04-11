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
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>TEEGRIXX</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/grixxtech'>GRIXXTECH</a>\n○ ANIME : <a href='https://t.me/Anime_Nation'>ANIME NATION</a>\n○ MANGA : <a href='https://t.me/Manga_Tron'>MANGATRON</a>\n○ ANIME ONGOING : <a href='https://t.me/AnimeNation_Ongoing'>ONGOING ANIMES</a></b>",
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
