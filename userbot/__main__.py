import os
import re
import sys
from pathlib import Path

import telethon.utils
from telethon import Button, TelegramClient, custom, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import InputMessagesFilterDocument

from userbot import LOGS, DYNAMICversion, bot
from userbot.Config import Config
from userbot.utils import (
    load_abuse,
    load_addons,
    load_module,
    start_assistant,
    start_spam,
)
from var import Var

l2 = Config.SUDO_COMMAND_HAND_LER
DYNAMIC_PIC = "https://telegra.ph/file/8e236edc9d8003679c21a.jpg"
l1 = Config.COMMAND_HAND_LER

firstname = replied_user.user.first_name


async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"DYNAMIC_STRING - {str(e)}")
        sys.exit()


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Var.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
            ).start(bot_token=Var.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("❤️ DYNAMIC USERBOT IS STARTING IN A DYNAMIC WAY ❤️")
            bot.loop.run_until_complete(add_bot(Config.BOT_USERNAME))
            LOGS.info("❤️‍🔥🔥 DYNAMIC USERBOT Startup Completed 🔥❤️‍🔥")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

print("📍⚜️Dynamic Plugins / Are Loading⚜️✔️")


async def module():
    import glob

    path = "userbot/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))


assistant = os.environ.get("ASSISTANT", None)


async def assistants():
    if assistant == "ON":
        import glob

        path = "userbot/plugins/assistant/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                start_assistant(shortname.replace(".py", ""))
    else:
        print("⚠️Assistant Not Loaded⚠️🤖")


addon = os.environ.get("EXTRA_PLUGIN", None)


async def addons():
    if addon == "ON":
        import glob

        path = "userbot/plugins/Xtra_Plugin/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                except Exception as e:
                    print(e)
    else:
        print("⚠️Addons Not Loading⚠️")


abuse = os.environ.get("ABUSE", None)


async def abuses():
    if abuse == "ON":
        import glob

        path = "userbot/plugins/Abuse/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                load_abuse(shortname.replace(".py", ""))
    else:
        print("⚠️Abuse Not Loading⚠️")


spam = os.environ.get("SPAM", None)


async def spams():
    if spam == "ON":
        import glob

        path = "userbot/plugins/Spam/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                start_spam(shortname.replace(".py", ""))
    else:
        print("⚠️Spam Not Loading⚠️")


# Assistant
tgbot = bot.tgbot


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"start")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="Hello {firstname} This Is The Dynamic Assistant ,How Can I Help You?",
            buttons=[
                [
                    custom.Button.inline("🙇 Usᴇʀs Lɪsᴛ 🙇", data="users"),
                    custom.Button.inline("👾 Cᴏᴍᴍᴀɴᴅs ✘👾", data="ibcmd"),
                ],
                [
                    Button.url(" Support ", "https://t.me/TheFriends_Zone"),
                    Button.url(" Updates ", "https://t.me/Dynamic_userbot"),
                ],
                [custom.Button.inline("⚙ Sᴇᴛᴛɪɴɢs ⚙", data="osg")],
                [custom.Button.inline("⚜ Hack ⚜", data="hck")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ules")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="🔰Rᴇᴀᴅ Tʜᴇ Rᴜʟᴇꜱ Tᴏᴏ🔰\n\n🔹 Dᴏɴ'ᴛ Sᴩᴀᴍ\n🔹 ᴛᴀʟᴋ Fʀɪᴇɴᴅʟy\n🔹 Dᴏɴ'ᴛ Bᴇ Rᴜᴅᴇ\n🔹 Sᴇɴᴅ Uʀ Mᴇꜱꜱᴀɢᴇꜱ Hᴇʀᴇ\n🔹 Nᴏ Pᴏʀɴᴏɢʀᴀᴘʜʏ\n🔹 Dᴏɴ'ᴛ Wʀɪᴛᴇ Bᴀᴅ Wᴏʀᴅs.\n\nWʜᴇɴ I Gᴇᴛ Fʀᴇᴇ Tɪᴍᴇ , I'ʟʟ Rᴇᴩʟy U 💯✅",
            buttons=[
                [
                    custom.Button.inline(
                        "🚫 Cʟᴏsᴇ 🚫",
                        data="lse_vcc",
                    )
                ],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lse_vcc")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lose")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile("live")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Wʜᴀᴛ Dᴏ Yᴏᴜ Wᴀɴᴛ Yᴏ Eᴅɪᴛ Iɴ Aʟɪᴠᴇ?\nFᴏʀ Aɴʏ Kɪɴᴅ Oғ Hᴇʟᴘ Dᴏ Jᴏɪɴ [ֆʊքքօʀȶ](https://t.me/thefriends_zone)**",
            buttons=[
                [
                    Button.inline("✘ Aʟɪᴠᴇ Nᴀᴍᴇ ✘", data="ame"),
                    Button.inline("✘ Aʟɪᴠᴇ Pɪᴄ ✘", data="mg"),
                ],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"mg")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Wʜɪᴄʜ Aʟɪᴠᴇ Pɪᴄ Dᴏ Yᴏᴜ Wᴀɴᴛ Tᴏ Cʜᴀɴɢᴇ?\nFᴏʀ Aɴʏ Kɪɴᴅ Oғ Hᴇʟᴘ Dᴏ Jᴏɪɴ [ֆʊքքօʀȶ](https://t.me/thefriends_zone)**",
            buttons=[
                [Button.inline("✘ Dᴇғᴀᴜʟᴛ Aʟɪᴠᴇ ✘", data="aig")],
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="live")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ame")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Yᴏᴜ Cᴀɴ Cʜᴀɴɢᴇ Aʟɪᴠᴇ Nᴀᴍᴇ..!!\nJᴜsᴛ Fᴏʟʟᴏᴡ Tʜᴇ Sᴛᴇᴘs.! \n\nFᴏʀ Aɴʏ Kɪɴᴅ Oғ Pʀᴏʙʟᴇᴍ Oʀ Dᴏᴜʙᴛ Dᴏ Jᴏɪɴ [ֆʊքքօʀȶ](https://t.me/thefriends_zone)\n\nJᴜsᴛ Tʏᴘᴇ\n\n`.set var ALIVE_NAME <Name>`\n\nRᴇᴍᴏᴠᴇ `<>` Tʜɪs.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="live")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"aig")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.alive`\nJust follow the steps.!\nAny kind of Problem or doubt do join [ֆʊքքօʀȶ](https://t.me/thefriends_zone)\n\nJust type\n\n`.set var ALIVE_PIC <Telegraph Link>`\n\nRemove `<>` this**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"dive")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.dalive` \nJust follow the steps.!\nAny kind of Problem or doubt do join [ֆʊքքօʀȶ](https://t.me/thefriends_zone)\n\nJust type\n\n`.set var AWAKE_PIC <Telegraph Link>`\n\nRemove `<>` this.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"aimg")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.alive`\nJust follow the steps.!\nAny kind of Problem or doubt do join [ֆʊքքօʀȶ](https://t.me/thefriends_zone)\n\nJust type\n\n`.set var ALIVE_PIC <Telegraph Link>`\n\nRemove `<>` this**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"dive")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.dalive` \nJust follow the steps.!\nAny kind of Problem or doubt do join [ֆʊքքօʀȶ](https://t.me/thefriends_zone)\n\nJust type\n\n`.set var AWAKE_PIC <Telegraph Link>`\n\nRemove `<>` this.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pmit")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**What do you want to edit in Pm Permit?\nFor Any kind of Problem or doubt do join [ֆʊքքօʀȶ](https://t.me/thefriends_zone)**",
            buttons=[
                [
                    Button.inline("✘ Pᴍ Pᴇʀᴍɪᴛ Tᴇxᴛ ✘", data="txt"),
                    Button.inline("✘ Pᴍ Pᴇʀᴍɪᴛ Mᴇᴅɪᴀ ✘", data="edia"),
                ],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"edia")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Pic permit Pic..!! \nJust follow the steps.!\nAny kind of Problem or doubt do join [ֆʊքքօʀȶ](https://t.me/thefriends_zone) type\n\n`.set var PM_PIC <Telegraph Link>`\n\nRemove `<>` this.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="pmit")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"txt")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Pic permit message..!! \nJust follow the steps.!\nAny kind of Problem or doubt do join [ֆʊքքօʀȶ](https://t.me/thefriends_zone)\n\nJust type\n\n`.set var PM_MSG <Text>`\n\nRemove `<>` this.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="pmit")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"osg")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Which type of setting do you want to edit?\nYou can change anything from these..!!\nAny kind for help do join [ֆʊքքօʀȶ](https://t.me/thefriends_zone)**",
            buttons=[
                [
                    Button.inline("✘ Aʟɪᴠᴇ ✘", data="live"),
                    Button.inline("✘ Pᴍ Pᴇʀᴍɪᴛ ✘", data="pmit"),
                ],
                [
                    Button.inline("✘ Chat Bot ✘", data="chat"),
                    Button.inline("✘ Vc Bot ✘", data="V_Bot"),
                ],
                [Button.inline("✘ Cʟᴏsᴇ ✘", data="lose")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ibcmd")))
async def users(event):
    await event.delete()
    grabon = "🇮🇳Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot \n➤ /purge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \n➤ /del - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"
    await tgbot.send_message(event.chat_id, grabon)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hck")))
async def users(event):
    await event.delete()
    grabon = "I am Giving U Full Power To Hack Anyone Through String session\nClick Here 👉/hack."
    await tgbot.send_message(event.chat_id, grabon)


async def DYNAMICs():
    DYNAMIC_USER = bot.me.first_name
    The_DON = bot.uid
    legd_mention = f"[{DYNAMIC_USER}](tg://user?id={The_DON})"
    yescaption = f"Hello Sir/Miss Something Happened \nDing Dong Ting Tong Ping Pong\nSuccessfully DYNAMICBOT Has Been Deployed \nMy Master ~ 『{legd_mention}』 \nVersion ~ {DYNAMICversion}\nClick Below To Know More About Me👇🏾👇👇🏼"
    try:
        TRY = [[Button.inline("⭐ Start ⭐", data="start")]]
        await tgbot.send_file(
            bot.me.id, DYNAMIC_PIC, caption=yescaption, buttons=TRY, incoming=True
        )
    except:
        pass


plc = os.environ.get("PLUGIN", None)


async def hekp():
    try:
        os.environ[
            "DYNAMIC_STRING"
        ] = "String Is A Sensitive Data \nSo Its Protected By DYNAMICBOT"
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                DYNAMIC_PIC,
                caption=f"Deployed ɖʏռǟʍɨƈ ʊֆɛʀɮօȶ Successfully\n\nɖʏռǟʍɨƈ ʊֆɛʀɮօȶ ~ {DYNAMICversion}\n\nType `{l1}help` or `{l1}ping` to check!\nFor Assistant Type `.on` \n\nJoin [DYNAMICBOT Channel](t.me/Dynamic_Userbot) for Updates & [DYNAMICBOT Chat](http://t.me/thefriends_zone) for any query regarding DYNAMICBOT",
            )
    except Exception as e:
        print(str(e))

    try:
        await bot(JoinChannelRequest("@Dynamic_Userbot"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@DYNAMIC_Userbot"))
    except BaseException:
        pass

    # try:
    # await bot(JoinChannelRequest("@DYNAMIC_UserbotPlugin"))
    # return
    # except BaseException:
    #  pass


async def install():
    if plc == "ON":
        try:
            await bot(JoinChannelRequest("@DYNAMIC_UserBotPlugin"))
        except BaseException:
            pass
        i = 0
        chat = -1001518412326
        documentss = await bot.get_messages(
            chat, None, filter=InputMessagesFilterDocument
        )
        total = int(documentss.total)
        total_doxx = range(0, total)
        for ixo in total_doxx:
            mxo = documentss[ixo].id
            downloaded_file_name = await bot.download_media(
                await bot.get_messages(chat, ids=mxo), "userbot/plugins/"
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                print(f"{i} plugin install")
            else:
                print("Failed")


bot.loop.run_until_complete(module())
bot.loop.run_until_complete(addons())
bot.loop.run_until_complete(abuses())
bot.loop.run_until_complete(assistants())
bot.loop.run_until_complete(spams())
bot.loop.create_task(hekp())
bot.loop.run_until_complete(install())

print(
    f"""
╔════❰DYNAMICBOT❱═❍⊱❁۪۪
║┣⪼ OWNER - {Config.ALIVE_NAME}
║┣⪼ Group - @TheFriends_Zone
║┣⪼ CREATOR - @Always_Don
║┣⪼ DYNAMICBOT - {DYNAMICversion}
║┣⪼ ✨ 『DYNAMIC』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱"""
)
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

bot.loop.run_until_complete(DYNAMICs())


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()
