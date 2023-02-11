list_a = [1, 0, True]
list_b = ['aaa', 'bb', 'c']


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Cat({self.name=}, {self.age=})'


if __name__ == '__main__':
    print(all(list_a))              # Вернет False, так как в списке есть 0
    print(any(list_a))              # Вернет True, так как один или несколоко элементов True
    print(max(list_b))              # Вернет c, ее порядковый номер в алфавите больше остальных элементов
    print(max(list_b, key=len))     # Вернет aaa, ее длина больше остальных элементов
    cats = [Cat('Tom', 3), Cat('Angela', 4), Cat('Bob', 5)]
    print(max(cats, key=lambda cat: cat.age))