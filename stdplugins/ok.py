"""Emoji

Available Commands:

tq"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="tq ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.00001
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
            "V",
            "E",
            "R",
            "Y",
            "M",
            "U",
            "C",
            "H",
            "😇🌷"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 18])
