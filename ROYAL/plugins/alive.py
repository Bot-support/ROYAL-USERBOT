# MADE BY ROYALOP 
# COPYRIGHT TO TEAM ROYAL 2021-2022 SHOULD NOT FOUND ANYWHERE ELSE YOU WILL GET GBAN AND WE WILL COPYRIGHT YOUR REPO.
import asyncio
import random
from telethon import events
from ROYAL.utils import admin_cmd
from telethon.tl.types import ChannelParticipantsAdmins
# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/57520dcef65f3b0d7e417.jpg"
file2 = "https://telegra.ph/file/57520dcef65f3b0d7e417.jpg"
file3 = "https://telegra.ph/file/57520dcef65f3b0d7e417.jpg"
file4 = "https://telegra.ph/file/57520dcef65f3b0d7e417.jpg"
file5 = "https://telegra.ph/file/57520dcef65f3b0d7e417.jpg"
file6 = "https://telegra.ph/file/57520dcef65f3b0d7e417.jpg"
file7 = "https://telegra.ph/file/57520dcef65f3b0d7e417.jpg"
pm_caption = "π₯π₯ **ROYAL IS WORKING PROPERLY LETS PARMTY..!! **π₯π₯\n\n"
pm_caption += "βοΈβοΈ ** THIS BOT BELOGS TO ROYALGANG**βοΈβοΈ\n\n"
pm_caption += "ββSππππ΄πΌ πππ°πππβββ\n\n"
pm_caption += "ββππ΄π»π΄ππ·πΎπ½ ππ΄πππΈπΎπ½ ββ : 1.19.5\n"
pm_caption += "fββ  ..π½ππππ πππππππ..ββ>> : 0.1\n"
pm_caption += "..π½ππππ πππππππ..|Support ββ : [GROUP](https://t.me/ROYAL_USERBOT_SUPPORT\n)"
pm_caption += "..π½ππππ πππππππ.. | CHANNELββ : [CHANNEL](https://t.me/ROYAL_USERBOT_OFFICIAL\n)"
@borg.on(admin_cmd(pattern=r"alive"))



async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file5)
      
    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file6)
    
    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(yes.chat_id, ok9, file=file7)

    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()
