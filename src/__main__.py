import asyncio
import logging

from src.setup import respond

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.FileHandler('app.log'))

asyncio.run(respond())
