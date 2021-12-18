import os

from telethon import Button, events

from userbot import *
from userbot.Config import Config
from userbot.plugins import *

DYNAMIC_IMG = os.environ.get(
    "BOT_PING_PIC", "https://telegra.ph/file/a9f6a3c160977352dd595.jpg"
)
ms = 4
ALIVE = Config.ALIVE_NAME

DON = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url("⚜ Lêɠêɳ̃dẞø† ⚜", "https://t.me/DYNAMIC_Userbot")]]
    await tgbot.send_file(event.chat_id, DYNAMIC_IMG, caption=DON, buttons=GOOD)
