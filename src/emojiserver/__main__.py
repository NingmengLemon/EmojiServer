import argparse

from aiohttp import web

from .server import app


parser = argparse.ArgumentParser(description="EmojiServer")

parser.add_argument("--port", type=int, default=8080, help="set port")

args = parser.parse_args()


web.run_app(app, port=args.port)
