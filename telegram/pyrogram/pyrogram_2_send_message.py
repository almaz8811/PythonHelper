from os import getenv
import time
from pyrogram import Client
from pyrogram.enums import ChatAction, ParseMode
from pyrogram.types import InputMediaPhoto

API_ID = getenv('API_ID')
API_HASH = getenv('API_HASH')

# Создаем клиент сессии с любым имением
client = Client(name='AlMaz_Pyrogram_One_App', api_id=API_ID, api_hash=API_HASH, parse_mode=ParseMode.HTML)

client.start()

# client.send_chat_action('almaz8812', ChatAction.TYPING)
# time.sleep(3)
# client.send_message('almaz8812', '**Привет, Александр**', parse_mode=ParseMode.MARKDOWN)
# client.send_chat_action('almaz8812', ChatAction.UPLOAD_PHOTO)
# time.sleep(3)
# client.send_photo('almaz8812', 'lotus pose_600.png', caption='<b>Lotus Pose</b>')
list_media = []
media_1 = InputMediaPhoto('lotus pose_600.png', caption='photo_1')
media_2 = InputMediaPhoto('lotus pose_600.png', caption='photo_2')
media_3 = InputMediaPhoto('lotus pose_600.png', caption='photo_3')
list_media.append(media_1)
list_media.append(media_2)
list_media.append(media_3)
client.send_chat_action('almaz8812', ChatAction.UPLOAD_PHOTO)
time.sleep(3)
client.send_chat_action('almaz8812', ChatAction.TYPING)
client.send_media_group('almaz8812', list_media)

client.stop()
