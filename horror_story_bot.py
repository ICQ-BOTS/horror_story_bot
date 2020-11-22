from handlers import *
from mailru_im_async_bot.bot import Bot
from mailru_im_async_bot.filter import Filter
from mailru_im_async_bot.handler import CommandHandler, DefaultHandler, StartCommandHandler, BotButtonCommandHandler
import logging
from logging.config import fileConfig
from pid import PidFile
import configparser
import asyncio
import sys
import os

configs_path = os.path.realpath(os.path.dirname(sys.argv[0])) + "/"

# Check exists config
if not os.path.isfile(os.path.join(configs_path, "logging.ini")):
    raise FileExistsError(f"File logging.ini not found in path {configs_path}")

# Read config
logging.config.fileConfig(os.path.join(configs_path, "logging.ini"), disable_existing_loggers=False)
log = logging.getLogger(__name__)
loop = asyncio.get_event_loop()

NAME = "horror_story"
TOKEN = "001.2918970001.1540231839:753423284"


bot = Bot(
    token=TOKEN, version=VERSION, name=NAME, poll_time_s=POLL_TIMEOUT_S, request_timeout_s=REQUEST_TIMEOUT_S,
    task_max_len=TASK_MAX_LEN, task_timeout_s=TASK_TIMEOUT_S
)

# Register your handlers here
# ---------------------------------------------------------------------
bot.dispatcher.add_handler(StartCommandHandler(callback=start))
bot.dispatcher.add_handler(DefaultHandler(callback=start))
bot.dispatcher.add_handler(BotButtonCommandHandler(
                            callback=story,
                            filters=Filter.callback_data('horro_story')
                        )
                    )


with PidFile(NAME):
    try:
        loop.create_task(bot.start_polling())
        loop.run_forever()
    finally:
        loop.close()
