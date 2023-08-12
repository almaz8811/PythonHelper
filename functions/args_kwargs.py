a, b, c = 1, 2, 3
d, *e = 1, 2, 3
*f, g = 'abcde'
i, *j, k = 'abcde'
l, *_, m = 'abcde'  # не хранит переменную _ (удобно использовать вместо срезов)


# / - все что слева - это позиционные аргументы
# * - все что слева - это keywords (ключевые) аргументы
def example(a, b, /, c, *, d):
    print(a)
    print(b)
    print(c)
    print(d)


# args собирает все позиционные аргументы в кортеж
def my_print(*args, number=1):
    for arg in args:
        print(str(arg) * number)

# kwargs собирает все keyword аргументы в словарь
def my_print_2(*args, **kwargs):
    print(f'Аргументы kwargs: {kwargs}')
    for arg in args:
        print(str(arg), **kwargs)   # можно передать распакованные аргументы в другую функцию

if __name__ == '__main__':
    print(f'{a=}')  # a=1
    print(f'{b=}')  # b=2
    print(f'{c=}')  # c=3

    # * условно обозначает "все остальное"
    print(f'{d=}')  # d=1
    print(f'{e=}')  # e=[2, 3] - * записывает все оставшиеся значения в переменную e

    print(f'{f=}')  # f=['a', 'c', 's', 'd'] - записывает все значения в переменную f кроме последнего значения
    print(f'{g=}')  # g='e'

    print(f'{i=}')  # i='a'
    print(f'{j=}')  # j=['b', 'c', 'd']
    print(f'{k=}')  # k='e'

    print(f'{l=}')  # l='a'
    print(f'{m=}')  # m='e'

    print(*[1, 2, 3])  # 1 2 3 - распаковка значений

    example(1, 2, c=3, d=4)
    print('================================================================')
    my_print(1, 2, 3, 4, number=2)
    my_print_2(1, 2, 3, 4, sep=':', end='-')
