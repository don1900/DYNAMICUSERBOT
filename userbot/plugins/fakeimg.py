import os

import requests

from DYNAMICBOT.utils import admin_cmd, sudo_cmd
from userbot import CmdHelp


@bot.on(admin_cmd(pattern="picgen"))
@bot.on(sudo_cmd(pattern="picgen", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return

    url = "https://thispersondoesnotexist.com/image"
    response = requests.get(url)
    await event.edit("`Creating a fake face...`")
    if response.status_code == 200:
        with open("DYNAMICBOT.jpg", "wb") as f:
            f.write(response.content)

    captin = f"Fake Image By DYNAMICBOT."
    fole = "DYNAMICBOT.jpg"
    await borg.send_file(event.chat_id, fole, caption=captin)
    await event.delete()
    os.system("rm /root/userbot/DYNAMICBOT.jpg ")


CmdHelp("fakeimg").add_command("picgen", None, "Fake Pic Generation").add()
