from userbot.events import register


@register(outgoing=True, pattern="^.yeet$")
async def edit_iterator(event):
    for i in range(44):
        await asyncio.sleep(0.08)
        try:
            await event.edit(f"`{i}`")
        except:
            pass
