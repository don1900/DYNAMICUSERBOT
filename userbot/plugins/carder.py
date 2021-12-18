from faker import Faker
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from DYNAMICBOT import CmdHelp
from DYNAMICBOT import bot as DYNAMICBOT
from DYNAMICBOT.utils import admin_cmd, edit_or_reply, sudo_cmd


@DYNAMICBOT.on(admin_cmd("gencc$"))
@DYNAMICBOT.on(sudo_cmd("gencc$", allow_sudo=True))
async def _(DYNAMICevent):
    if DYNAMICevent.fwd_from:
        return
    DYNAMICcc = Faker()
    DYNAMICname = DYNAMICcc.name()
    DYNAMICadre = DYNAMICcc.address()
    DYNAMICcard = DYNAMICcc.credit_card_full()

    await edit_or_reply(
        DYNAMICevent,
        f"__**👤 NAME :- **__\n`{DYNAMICname}`\n\n__**🏡 ADDRESS :- **__\n`{DYNAMICadre}`\n\n__**💸 CARD :- **__\n`{DYNAMICcard}`",
    )


@DYNAMICBOT.on(admin_cmd(pattern="bin ?(.*)"))
@DYNAMICBOT.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    DYNAMIC_input = event.pattern_match.group(1)
    chat = "@szbinscheckerbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2143004427)
            )
            await event.client.send_message(chat, f"/bin {DYNAMIC_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @szbinscheckerbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@DYNAMICBOT.on(admin_cmd(pattern="register ?(.*)"))
@DYNAMICBOT.on(sudo_cmd(pattern="register ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    DYNAMIC_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/register {DYNAMIC_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@DYNAMICBOT.on(admin_cmd(pattern="password ?(.*)"))
@DYNAMICBOT.on(sudo_cmd(pattern="password ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    DYNAMIC_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/password {DYNAMIC_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


CmdHelp("carder").add_command("gencc", None, "Generates fake cc...").add_command(
    "register", None, "Register Ur Account Here"
).add_command("password", "<enter>", "Set ur Account Password On CXM.CARDS").add()
