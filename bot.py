import os
import json
import logging

from aiohttp import get
from aiotg import TgBot

INVITE_TEXT = "%s has started a video conference in room: [%s](%s)"
ROOM_API = "https://api.appear.in/random-room-name"

with open("config.json") as cfg:
    config = json.load(cfg)

bot = TgBot(**config)
logger = logging.getLogger("appear.in")


@bot.command(r"/appear")
async def echo(chat, match):
    async with get(ROOM_API) as res:
        room = (await res.json())["roomName"][1:]
        user = chat.sender["first_name"]
        url = "https://appear.in/" + room
        invite = INVITE_TEXT % (user, room, url)
        logger.info("%s created room '%s'", user, room)
        await chat.send_text(invite, parse_mode="Markdown")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    bot.run()
