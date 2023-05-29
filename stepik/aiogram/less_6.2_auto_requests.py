import requests
import time
import os

'''
##### 6.2.3 #####
Автоматизируем запросы к Telegram Bot API
'''

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = os.getenv('TOKEN')
TEXT = 'Пришел апдейт!'
MAX_COUNTER = 100  # Количество интераций цикла

offset = -2  # Чтобы получать апдейты, которые мы еще не получали
counter = 0
chat_id: int

while counter < MAX_COUNTER:
    print(f'attempt = {counter}')  # Чтобы видеть в консоли, что код работает
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
    time.sleep(1)
    counter += 1

'''
##### 6.2.4 #####
Сформируйте и вставьте в поле ниже URL запроса к Telegram Bot API,
который отправит пользователю текстовое сообщение "AMAZING!"

https://api.telegram.org/bot<token>/sendMessage?chat_id=<chat_id>&text=AMAZING!
'''
