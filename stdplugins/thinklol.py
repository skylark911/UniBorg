# (c) @UniBorg

from telethon import events
import asyncio
from collections import deque


@borg.on(events.NewMessage(pattern=r"\.lul", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🤔🧐🤔🧐🤔🧐"))
	for _ in range(50):
		await asyncio.sleep(1.0)
		await event.edit("".join(deq))
		deq.rotate(1)
    
