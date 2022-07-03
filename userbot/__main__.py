import sys

import userbot
from userbot import BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import legend
from .start import killer
from .utils import (
    add_bot_to_logger_group,
    hekp,
    load_plugins,
    setup_bot,
    spams,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("LegendUserBot")

print(userbot.__copyright__)
print(f"Licensed under the terms of the {userbot.__license__}")

cmdhr = Config.HANDLER


try:
    LOGS.info("Starting Userbot")
    legend.loop.run_until_complete(setup_bot())
    LOGS.info("TG Bot Startup Completed")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    await killer()
    # await scammer("Godmrunal")
    await spams()
    print("----------------")
    print("Starting Bot Mode!")
    print("⚜ LegendBot Has Been Deployed Successfully ⚜")
    print("OWNER - @LegendBoy_XD")
    print("Group - @LegendBot_XD")
    print("----------------")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    return


legend.loop.run_until_complete(startup_process())
legend.loop.create_task(hekp())

if len(sys.argv) in {1, 3, 4}:
    try:
        legend.run_until_disconnected()
    except ConnectionError:
        pass
else:
    legend.disconnect()
