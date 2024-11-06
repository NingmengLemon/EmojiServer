import os

import aiofiles
from aiohttp import web

from .dataset import EmojiDataset


dataset = EmojiDataset()
dataset.load()


async def handle_request(request: web.Request):
    path = request.match_info.get("path", "").strip("/")
    emoji_text = path
    emoji_data = dataset.get_emoji(emoji_text)

    if not emoji_data:
        return web.Response(text="Emoji not found", status=404)

    async with aiofiles.open(
        os.path.join("img-google-136", emoji_data["image"]), "rb"
    ) as fp:
        return web.Response(body=await fp.read(), content_type="image/png")


app = web.Application()
app.router.add_get("/{path:.*}", handle_request)
