from os import getenv
from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

API_ID = getenv('API_ID')
API_HASH = getenv('API_HASH')

# Создаем клиент сессии с любым имением
client = Client(name='AlMaz_Pyrogram_One_App', api_id=API_ID, api_hash=API_HASH)


# В функцию обработки события приходят объект клиента и сообщения
# def all_message(client: Client, message: Message):
#     message.reply(message.text, quote=True, reply_to_message_id=message.id)  # Ответ с цитированием на id сообщения
#     # message.reply(message.text, quote=True)   # Ответ с цитированием
#     # message.reply(message.text, reply_to_message_id=message.id) # Ответ с цитированием
#     # message.reply(message.text, quote=False)  # Ответ без цитирования


# Функция обработки событий с декоратором, для нее не требуется регистрировать обработчик add_handler
@client.on_message()
def all_message_decorator(client: Client, message: Message):
    # message.copy('me')  # Копировать сообщение в избранное
    # message.copy('almaz8811')  # Копировать сообщение в избранное по user_name
    # message.copy('132103826')  # Копировать сообщение в избранное по user_id
    # message.forward('me')  # Переслать сообщение в избранное
    # message.reply(message.text, quote=True, reply_to_message_id=message.id) # Ответ с цитированием на id сообщения
    # client.send_message(message.chat.id, message.text)  # Отправить сообщение в этот же чат с помощью клиента
    # client.forward_messages('me', message.chat.id, message.id)  # Переслать сообщение в этот же чат с помощью клиента
    client.copy_message('me', message.chat.id, message.id, disable_notification=True)  # Отправка без звука


# Добавляем обработчик на любое сообщение
# client.add_handler(MessageHandler(all_message))


# # Отправить себе сообщение в избранное
# client.start()
# client.send_message('me', 'Сообщение')
# client.stop()

# Запускаем клиент
client.run()
