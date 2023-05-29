import requests
import time
import os

'''
##### 6.3.2 #####
Long Poling
Чтобы снизить нагрузку от большого количества частых запросов, Телеграм-сервера могут работать в режиме лонг поллинга.
Long polling - это polling "с ожиданием апдейтов", то есть происходит соединение с сервером
на определенное время (timeout). Если апдейты есть - сервер их отправляет и закрывает соединение,
а если нет - то соединение остается открытым в течение этого времени. Если апдейты за это время появляются -
сервер их отправляет и сразу закрывает соединение, а если не появляются, то соединение закрывается по истечении времени
таймаута. Затем процесс обращения к серверу повторяется.
'''

API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = os.getenv('TOKEN')
offset: int = -2
timeout: int = 10
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')
