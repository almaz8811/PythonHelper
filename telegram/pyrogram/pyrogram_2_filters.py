from os import getenv
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

API_ID = getenv('API_ID')
API_HASH = getenv('API_HASH')

# Создаем клиент сессии с любым имением
client = Client(name='AlMaz_Pyrogram_One_App', api_id=API_ID, api_hash=API_HASH, parse_mode=ParseMode.HTML)


def message_text(client: Client, message: Message):
    message.reply('Вы отправили текст', quote=True)


def message_photo(client: Client, message: Message):
    message.reply('Вы отправили фото', quote=True)


def message_sticker(client: Client, message: Message):
    message.reply('Вы отправили стикер', quote=True)


media = []


def message_mediagroup(client: Client, message: Message):
    if message.media_group_id in media:
        return
    else:
        media.append(message.media_group_id)
    message.reply('Вы отправили набор фото', quote=True)


# client.add_handler(MessageHandler(message_text, filters=filters.text & filters.chat(chats='almaz8811')))
client.add_handler(
    MessageHandler(message_text, filters=filters.text & (~filters.outgoing & ~filters.chat(chats='me'))))
client.add_handler(MessageHandler(message_mediagroup, filters=filters.media_group))
client.add_handler(MessageHandler(message_photo, filters=filters.photo))
client.add_handler(MessageHandler(message_sticker, filters=filters.sticker))

client.run()
