from pyrogram import Client, filters
# from pyrogram.errors import FloodWait
import logging
import os

bot_token = os.environ.get('BOT_TOKEN')
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')

logging.basicConfig(level=logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# Initialize the client and set the API_ID and API_HASH
app = Client("forwardcover", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Handle the commands
@app.on_message(filters.command('start') & filters.private)
async def start(app, message):
    await message.reply_text(f"Hi {message.from_user.first_name}!, I'm simple forward cover bot.\nI will echo everything you send.", quote=True)
    logging.info(f'{message.from_user.id} started the bot.')

@app.on_message(filters.text & filters.private)
async def text(app, message):
    await message.reply_text(message.text)
    await message.delete()

@app.on_message(filters.photo & filters.private)
async def ephoto(app, message):
    file_id = message.photo.file_id
    await app.send_photo(chat_id=message.from_user.id, photo=file_id)
    await message.delete()

@app.on_message(filters.video & filters.private)
async def evideo(app, message):
    file_id = message.video.file_id
    await app.send_video(chat_id=message.from_user.id, video=file_id)
    await message.delete()


@app.on_message(filters.document & filters.private)
async def edoc(app, message):
    file_id = message.document.file_id
    await app.send_document(chat_id=message.from_user.id, document=file_id)
    await message.delete()

@app.on_message(filters.audio & filters.private)
async def eaudio(app, message):
    file_id = message.audio.file_id
    await app.send_audio(chat_id=message.from_user.id, audio=file_id)
    await message.delete()

@app.on_message(filters.voice & filters.private)
async def evoice(app, message):
    file_id = message.voice.file_id
    await app.send_voice(chat_id=message.from_user.id, voice=file_id)
    await message.delete()

app.run()
