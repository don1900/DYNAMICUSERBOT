from telethon import events

from userbot import *

from . import *

PM_IMG = "https://telegra.ph/file/c26fc61e904476083baa7.jpg"
pm_caption = f"⚜『Lêɠêɳ̃dẞø†』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『{DYNAMIC_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣『Lêɠêɳ̃dẞø†』~ `{DYNAMICversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/Its_DYNAMICBOT)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/don1900/LEGENBOT/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [『Lêɠêɳ̃dẞø†』 ](https://t.me/DYNAMIC_Userbot)\n"
pm_caption += f"┣Assistant ~ By [『Lêɠêɳ̃dẞøy』 ](https://t.me/Its_DON)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『Lêɠêɳ̃dẞø†』](https://t.me/DYNAMIC_Userbot) «««"


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
