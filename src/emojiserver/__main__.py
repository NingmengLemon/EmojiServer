from aiohttp import web

from .server import app


web.run_app(app, port=8080)
