from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "file_separator_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

media_groups = {}

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        "✅ File Separator Bot Started!\n\n"
        "Send media albums or multiple files and I will separate them automatically."
    )

@app.on_message(filters.media_group)
async def handle_media_group(client, message: Message):
    group_id = message.media_group_id

    if group_id not in media_groups:
        media_groups[group_id] = []

    media_groups[group_id].append(message)

    await asyncio.sleep(2)

    if len(media_groups[group_id]) > 0:
        msgs = media_groups[group_id]

        for msg in msgs:
            try:
                await msg.copy(message.chat.id)
            except Exception as e:
                print(e)

        del media_groups[group_id]

print("✅ Bot Started...")
app.run()
