from DYNAMICBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import bot
from userbot.cmdhelp import CmdHelp
from userbot.helpers.funct import deEmojify


@bot.on(admin_cmd(pattern="mev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mev(?: |$)(.*)", allow_sudo=True))
async def nope(DYNAMIC):
    DYNAMIC = DYNAMIC.pattern_match.group(1)
    if not DYNAMIC:
        if DYNAMIC.is_reply:
            (await DYNAMIC.get_reply_message()).message
        else:
            await edit_or_reply(
                DYNAMIC,
                "`Sir please give some query to search and download it for you..!`",
            )
            return

    troll = await bot.inline_query("TrollVoiceBot", f"{(deEmojify(DYNAMIC))}")

    await troll[0].click(
        DYNAMIC.chat_id,
        reply_to=DYNAMIC.reply_to_msg_id,
        silent=True if DYNAMIC.is_reply else False,
        hide_via=True,
    )
    await DYNAMIC.delete()


CmdHelp("memevoice").add_command(
    "mev", "<meme txt>", "Searches and uploads the meme in voice format (if any)."
).add()
