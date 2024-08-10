import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from EsproAiMusic import LOGGER, app, userbot
from EsproAiMusic.core.call import EsproAi
from EsproAiMusic.misc import sudo
from EsproAiMusic.plugins import ALL_MODULES
from EsproAiMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS
from stem import Signal
from stem.control import Controller
import asyncio
import threading

async def change_tor_ip(control_port=9050, timeout=10):
    try:
        with Controller.from_port(port=control_port) as controller:
            controller.authenticate()  # Authenticate with the control port
            controller.signal(Signal.NEWNYM)  # Request a new IP address
            await asyncio.sleep(timeout)  # Wait for the new IP to be established
            print("Tor IP address changed successfully.")
    except Exception as e:
        print(f"Failed to change Tor IP: {e}")

async def periodic_ip_rotation(interval=180, control_port=9050, timeout=10):
    while True:
        await change_tor_ip(control_port, timeout)
        await asyncio.sleep(interval)  # Wait for the specified interval before changing IP again

def run_periodic_ip_rotation():
    asyncio.run(periodic_ip_rotation())




async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("EsproAiMusic.plugins" + all_module)
    LOGGER("EsproAiMusic.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await userbot.start()
    await EsproAi.start()
    try:
        await EsproAi.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("EsproAiMusic").error(
            "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧\𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n\n𝗧𝗠𝗠 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........"
        )
        exit()
    except:
        pass
    await EsproAi.decorators()
    LOGGER("EsproAiMusic").info(
        "EsproAiMusic stated jaao enjoy karo \n Please 🥺 aapna gf haiwan ko de do please please please please 🥺🥺🥺🥺.."
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("EsproAiMusic").info("𝗦𝗧𝗢𝗣 𝗧𝗠𝗠 𝗠𝗨𝗦𝗜𝗖🎻 𝗕𝗢𝗧..")


if __name__ == "__main__":
    ip_rotation_thread = threading.Thread(target=run_periodic_ip_rotation)
    ip_rotation_thread.start()
    asyncio.get_event_loop().run_until_complete(init())
