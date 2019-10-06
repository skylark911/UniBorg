"""Emoji

Available Commands:

tq"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd

@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.0
    animation_ttl = range(0, 90)
    input_str = event.pattern_match.group(1)
    if input_str == "tq":
        await event.edit(input_str)
        animation_chars = [
            "T",
            "H",
            "A",
            "N",
            "K",
            "Y",
            "O",
            "U",
            "THANK YOU 😇🌷"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 9])
