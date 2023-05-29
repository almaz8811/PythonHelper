import requests


def response(url: str) -> str | int:
    resp = requests.get(url)  # Отправляем GET запрос и сохраняем ответ в переменной response
    if resp.status_code == 200:  # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
        return resp.text
    else:
        return resp.status_code  # При другом коде ответа выводим этот код


api_url = 'http://api.open-notify.org/iss-now.json'
print(response(api_url))

'''
Сделайте запрос к API http://numbersapi.com/ для числа 43 и скопируйте в текстовое поле полный ответ от сервиса.
Примечание. Ответ не должен содержать в себе дополнительных символов (пробелов, переносов строки и т.п.)
он должен быть ровно таким, каким его прислал сервис. 
'''

api_url = 'http://numbersapi.com/43'
print(response(api_url))
