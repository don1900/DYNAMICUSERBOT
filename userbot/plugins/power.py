import os
import sys

from DYNAMICBOT.utils import admin_cmd, eor, sudo_cmd
from userbot import HEROKU_APP, DYNAMICversion, bot
from userbot.cmdhelp import CmdHelp
from userbot.helpers.runner import reload_DYNAMICBOT


@bot.on(admin_cmd(pattern="restart"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("яєϐοοτιиg **[ ░░░ ]** ...\nωαιτ ƒєω мιиυτє⚠️")
    await event.edit("яєϐοοτιиg **[ █░░ ]** ...\nωαιτ ƒєω мιиυτє☣️")
    await event.edit("яєϐοοτιиg **[ ██░ ]** ...\nωαιτ ƒєω мιиυτє☢️")
    await event.edit("яєϐοοτιиg **[ ███ ]** ...\nωαιτ ƒєω мιиυτєѕ☢️")
    await event.edit(
        f"Rebooted 𝕷𝐞̂𝐠𝐞́𝐧̃𝐝𝕭ø𝖙 {DYNAMICversion} **[ ✔️ ]** ...\nType `.ping` or `.DYNAMIC` after 5min to check if I am working✔️"
    )
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@bot.on(admin_cmd(pattern="shutdown$"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(
        "**[ ! ]** `⚰️Turning off bot now ... Manually turn me on later or follow step of update in @DYNAMIC_Userbot` ಠ_ಠ"
    )
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["userbot"].scale(0)
    else:
        sys.exit(0)


@bot.on(admin_cmd(pattern="reload$"))
@bot.on(sudo_cmd(pattern="reload$", allow_sudo=True))
async def rel(event):
    await eor(event, "Reloading Lêɠêɳ̃dẞø†... Wait for few seconds...")
    await reload_DYNAMICBOT()


CmdHelp("power").add_command(
    "restart",
    None,
    "Restarts your userbot. Reѕtarting Bot may result in better functioning of bot when its laggy",
).add_command(
    "shutdown",
    None,
    "Turns off Dynos of Userbot. Userbot will stop working unless you manually turn it on from heroku",
).add_command(
    "reload", None, "Reload Ur All Plugins"
).add_info(
    "Power Button Command Of Bot"
).add_warning(
    "✅ Harmless Module"
).add_type(
    "Official"
).add()
