import os
import json

from aiohttp import get
from aiotg import TgBot

INVITE_TEXT = "%s has started a video conference in room: [%s](%s)"
ROOM_API = "https://api.appear.in/random-room-name"

with open("config.json") as cfg:
    config = json.load(cfg)

bot = TgBot(**config)


@bot.command(r"/appear")
async def echo(chat, match):
    async with get(ROOM_API) as res:
        rname = (await res.json())["roomName"][1:]
        url = "https://appear.in/" + rname
        invite = INVITE_TEXT % (chat.sender["first_name"], rname, url)
        await chat.send_text(invite, parse_mode="Markdown")


if __name__ == '__main__':
    bot.run()
