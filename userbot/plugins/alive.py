import time

from telethon import version
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from DYNAMICBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import ALIVE_NAME, DYNAMICversion
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config

from . import *


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))
DEFAULTUSER = ALIVE_NAME or "ɖʏռǟʍɨƈẞø✞︎ 🇮🇳"
DYNAMIC_IMG = "https://telegra.ph/file/8e236edc9d8003679c21a.jpg"
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "ɛǟֆȶ օʀ աɛֆȶ ɖʏռǟʍɨƈ ʊֆɛʀɮօȶ ɨֆ ȶɦɛ աɛֆȶ"
CUSTOM_YOUR_GROUP = Config.YOUR_GROUP or "@DYNAMIC_Userbot"

DYNAMIC = bot.uid
mention = f"[{DEFAULTUSER}](tg://user?id={DYNAMIC})"


@bot.on(admin_cmd(outgoing=True, pattern="DYNAMIC$"))
@bot.on(sudo_cmd(pattern="DYNAMIC$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if DYNAMIC_IMG:
        DYNAMIC_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"

        DYNAMIC_caption += f"ɖʏռǟʍɨƈ ɮօȶ ɨֆ աօʀӄɨռɢ քɛʀʄɛƈȶʟʏ\n\n"
        DYNAMIC_caption += f"        **🔥ɖʏռǟʍɨƈ ֆʏֆȶɛʍ🔥** \n\n"
        DYNAMIC_caption += f"•⭕️• **ʍʏ ʍǟֆȶɛʀ**          ~ {ALIVE_NAME}\n"
        DYNAMIC_caption += f"•⭕️• **ɖʏռǟʍɨƈẞø✞︎ ʋɛʀֆɨօռ**   ~ {DYNAMICversion}\n"
        DYNAMIC_caption += f"•⭕️• **ȶɛʟɛȶɦօռ ʋɛʀֆɨօռ**     ~ `{version.__version__}`\n"
        DYNAMIC_caption += f"•⭕️• **ʊքȶɨʍɛ**         ~ `{uptime}`\n"
        DYNAMIC_caption += f"•⭕️• **ɢʀօʊք**           ~ [𝙶𝚛𝚘𝚞𝚙](t.me/TheFriends_Zone)\n"
        DYNAMIC_caption += f"•⭕️• **ɱყ ɢʀօʊք**  ~ {CUSTOM_YOUR_GROUP}\n"

        await alive.client.send_file(
            alive.chat_id, DYNAMIC_IMG, caption=DYNAMIC_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"         \n"
            f"•⚡• ȶɛʟɛȶɦօռ ʋɛʀֆɨօռ   : `{version.__version__}`\n"
            f"🇮🇳 ɖʏռǟʍɨƈẞø✞︎  : `{DYNAMICversion}`\n"
            f"🇮🇳 ʊքȶɨʍɛ        : `{uptime}`\n"
            f"🔱 ʍʏ ʍǟֆȶɛʀ        : {mention}\n"
            f"🔱 σωɳεɾ         : [ℓєgєи∂](t.me/Always_DON)\n",
        )


msg = f"""
**DYNAMIC BOT IS WORKING PERFECTLY**

       {Config.ALIVE_MSG}
    **  SYSTEM STATUS **
**•⚜️•OWNER    :** **{mention}**
**•🌹•DYNAMIC STATUS  :** {DYNAMICversion}
**•🌹•TELETHON  :** {version.__version__}
**•🌹•ABUSE     :**  {abuse_m}
**•🌹•SUDO      :**  {is_sudo}
**•🌹•BOT      :** {Config.BOY_OR_GIRL}
"""
botname = Config.BOT_USERNAME


@bot.on(admin_cmd(pattern="alive$"))
@bot.on(admin_cmd(pattern="alive$", allow_sudo=True))
async def DYNAMIC_a(event):
    try:
        DYNAMIC = await bot.inline_query(botname, "alive")
        await DYNAMIC[0].click(event.chat_id)
        if event.sender_id == The_DON:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command("bot", None, "υѕє αи∂ ѕєє").add_command(
    "DYNAMIC", None, "Its Same Like Alive"
).add_command("alive", None, "Its Show ur Alive Template").add_warning(
    "Harmless Module✅"
).add_info(
    "Checking Alive"
).add_type(
    "Official"
).add()
