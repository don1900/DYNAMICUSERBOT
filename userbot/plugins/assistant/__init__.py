# DYNAMICBOT Assistant
from telethon import Button, custom

from userbot import ALIVE_NAME, bot

from . import *

OWNER_NAME = ALIVE_NAME
OWNER_ID = bot.uid


DYNAMIC_USER = bot.me.first_name
Its_DON = bot.uid

DYNAMIC_mention = f"[{DYNAMIC_USER}](tg://user?id={Its_DON})"
DYNAMIC_logo = "./userbot/resources/pics/-6163428037589314866_121.jpg"
DYNAMIC_logo1 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
DYNAMIC_logo2 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
DYNAMIC_logo4 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
DYNAMIC_logo3 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
DYNAMICversion = "𝚅2.1"

perf = "[ †hê Lêɠêɳ̃dẞø† ]"


DEVLIST = ["2082798662"]


async def setit(event, name, value):
    try:
        event.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
