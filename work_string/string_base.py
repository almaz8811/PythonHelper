'''
Методы strip(), lstrip(), rstrip()
strip() - возвращает копию строки, удаляя как начальные, так и конечные символы (в зависимости от переданного строкового
аргумента). Синтаксис: string.strip([chars])
lstrip() - удаляет символы слева, rstrip() - удаляет символы справа
'''
text = '_Проверочный текст___'
# Если не указанны аргументы, то удаляться будут пробелы слева и справа
s = text.strip('_')  # Проверочный текст
print(s)
s = text.lstrip('_')  # Проверочный текст___
print(s)
s = text.rstrip('_')  # _Проверочный текст
print(s)

'''
Метод replase(old: str, new: str [, max_coutn: int]
Возвращает копию строки, в которой значения old заменены на new. Если не указать количество замен max_count,
то произойдет замена всех частей в тексте.
'''
s = text.replace('о', 'А')  # _ПрАверАчный текст___
print(s)
s = text.replace('о', 'А', 1)  # _ПрАверочный текст___
print(s)