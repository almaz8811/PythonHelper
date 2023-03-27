import re

# \d - decimal - Набор цифр
# \b..\b - в границах слова (не включает в себя запятые, скобки, пробелы и т.д.)
# \W - все слова, + - игнорируя знаки препинания

text = '''История России насчитывает более тысячи лет, начиная с переселения восточных славян на Восточно-Европейскую 
равнину в VI—VII веках, впоследствии разделившихся на русских, украинцев и белорусов[1]. История страны разделяется 
примерно на семь периодов: древнейший (догосударственный) (до конца IX века н. э.) период, период Киевской Руси 
(до середины XII века), период раздробленности (до начала XVI века), период единого Русского государства 
(с 1547 года царства) (конец XV века — 1721), период Российской империи (1721-1917), советский период (1917-1991) 
и новейшая история (с 1991)[2].'''

info = '10 EUR 20 EUR 30 EUR - EURO EUROPE'

text_2 = '''Знаки препинания: первая и вторая запятая - причастный оборот, третья запятая - подчинительная связь между 
предложениями, четвертая запятая - сочинительная связь между предложениями, пятая запятая - сочинительная связь между 
предложениями, шестая запятая - подчинительная связь между предложениями, седьмая запятая - подчинительная связь между 
предложениями'''

# r - использовать сырые данные raw (игнорировать спецсимволы
years = re.findall(r'\d{4}', text)   # \d - decimal (цифры), {4} - последовательность из 4-х подряд
print(years)

period = re.findall(r'\d{4}-\d{4}', text)
print(period)   # 1721—1917 вернет только периоды

result = re.sub(r'\bEUR\b', 'USD', info)
print(result)

words = re.split(r'\W+', text_2)    # \W - все слова, + - игнорируя знаки препинания
print(words)