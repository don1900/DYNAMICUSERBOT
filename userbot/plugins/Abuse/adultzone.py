# credits to userge
# ported to DYNAMICBOT by @Its_DON
# will be adding more soon

import asyncio
import os
import urllib

import requests

from userbot import *
from userbot.Config import Config
from userbot.utils import *


@bot.on(admin_cmd("boobs$"))
@bot.on(sudo_cmd(pattern="boobs$", allow_sudo=True))
async def boobs(event):
    if event.fwd_from:
        return
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await event.reply("Finding some big boobs for u 🧐")
    await asyncio.sleep(0.5)
    await a.edit("Sending Some Bigs Boobs")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


@bot.on(admin_cmd("butts$"))
@bot.on(sudo_cmd(pattern="butts$", allow_sudo=True))
async def butts(event):
    if event.fwd_from:
        return
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "butts.jpg")
    a = await event.reply("Finding some beautiful butts for u🧐")
    await asyncio.sleep(0.5)
    await a.edit("Sending some beautiful butts🤪")
    nsfw = requests.get("http://api.obutts.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


CmdHelp("adultzone").add_command("boobs", None, "Sends a random boobs pic").add_command(
    "butts", None, "Sends a random Butt pic"
).add_info("Use at Night Its Send U bad pic").add_warning("18+").add_type("Abuse").add()
