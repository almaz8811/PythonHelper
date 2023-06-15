'''
##### 7.4.2 #####
Функция custom_filter()
Реализуйте функцию custom_filter(), которая на вход принимает список some_list, с любыми типами данных,
находит в этом списке целые числа, отбирает из них те, что делятся нацело на 7, суммирует их,
а затем проверяет, превышает эта сумма 83 или нет. Если НЕ превышает - функция должна вернуть True,
если превышает - False.
'''


def custom_filter(some_list):
    return sum(filter(lambda x: isinstance(x, int) and x % 7 == 0, some_list)) <= 83


print(custom_filter([7, 14, 28, 32, 32, '56']))

'''
##### 7.4.3 #####
Анонимная функция как фильтр
Напишите функцию anonymous_filter, используя синтаксис анонимных функций, которая принимает строковый аргумент
и возвращает значение True, если количество русских букв я не меньше 23 (регистр буквы неважен)
и False в противном случае.
Примечание. Вызывать анонимную функцию не нужно. Только дописать ее код.
'''


def anonymous_filter(s):
    return sum(map(lambda x: 1 if 'я' in x.lower() else 0, s)) >= 23


print(anonymous_filter('яяzzzzzzzzzzzzzzzzzzzяяяяяяяяяяяяяяяяяяяяяяяя аваяЯ'))

'''
##### 7.4.5 #####
Встроенные фильтры в aiogram

# Фильтр Command([start]) и CommandStart работают одинаково
# Фильтр Text
# @dp.message(Text(endswith=['бот'], ignore_case=True)) заканчивается на 'bot' и игнорирует регистр

Полностью совпадает с каким-то текстом: Text(text='какой-то текст')
Начинается с какого-то конкретного текста: Text(startswith='начало какого-то текста')
Заканчивается каким-то текстом: Text(endswith='конец какого-то текста')
Содержит в себе какой-то текст: Text(contains='какой-то текст')

В виде коллекции:
Text(text=['какой-то текст 1', 'какой-то текст 2', 'какой-то текст 3'])
Text(startswith=('начало 1', 'начало 2', 'начало 3'))
Text(endswith={'конец 1', 'конец 2', 'конец 3'})
Text(contains=['какой-то текст 1', 'какой-то текст 2', 'какой-то текст 3'])
'''

'''
##### 7.4.6 #####
Магические фильтры
'''
from aiogram import F
from aiogram.types import ContentType

# Использование фильтров через F-экземпляр класса MagicFilter
F.photo  # Фильтр для фото
F.voice  # Фильтр для голосовых сообщений
F.content_type.in_({ContentType.PHOTO,
                    ContentType.VOICE,
                    ContentType.VIDEO})  # Фильтр на несколько типов контента
F.text == 'привет'  # Фильтр на полное совпадение текста
F.text.startswith('привет')  # Фильтр на то, что текст сообщения начинается с 'привет'
~F.text.endswith('bot')  # Инвертирование результата фильтра

# Примеры фильтров через lambda:
lambda message: message.photo  # Фильтр для фото
lambda message: message.voice  # Фильтр для голосовых сообщений
lambda message: message.content_type in {ContentType.PHOTO,
                                         ContentType.VOICE,
                                         ContentType.VIDEO}  # Фильтр на несколько типов контента
lambda message: message.text == 'привет'  # Фильтр на полное совпадение текста
lambda message: message.text.startswith('привет')  # Фильтр на то, что текст сообщения начинается с 'привет'
lambda message: not message.text.startswith('bot')  # Инвертирование результата фильтра

# Фильтр, который будет пропускать только апдейты от пользователя с ID = 173901673
lambda message: message.from_user.id == 173901673  # Через lambda
F.from_user.id == 173901673  # Через F

# Фильтр, который будет пропускать только апдейты от админов из списка 193905674, 173901673, 144941561
lambda message: message.from_user.id in {193905674, 173901673, 144941561}  # Через lambda
F.from_user.id.in_({193905674, 173901673, 144941561})  # Через F:

# Фильтр, который будет пропускать апдейты текстового типа, кроме тех, которые начинаются со слова "Привет"
lambda message: not message.text.startswith('Привет')  # Через lambda
~F.text.startswith('Привет')  # Через F

# Фильтр, который будет пропускать апдейты любого типа, кроме фото, видео, аудио и документов.
lambda message: not message.content_type in {ContentType.PHOTO,
                                             ContentType.VIDEO,
                                             ContentType.AUDIO,
                                             ContentType.DOCUMENT}  # Через lambda
~F.content_type.in_({ContentType.PHOTO,
                     ContentType.VIDEO,
                     ContentType.AUDIO,
                     ContentType.DOCUMENT})  # Через F
