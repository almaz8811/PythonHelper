# inheritence - наследование, это механизм получения доступа к данным и поведению своего предка

class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):  # задает оформление строки вывода
        return f'{self.__class__.__name__} {self.name}, salary={self.salary}, bonus={self.bonus}%,' \
               f' total bonus= {self.calculate_total_bonus()} rub'


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 15000, 1)


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 45000, 15)


class CEO(Employee):
    def __init__(self, name):
        super().__init__(name, 105000, 100)

# class CEO:
#     def __init__(self, name):
#         self.name = name
#         self.salary = 105000
#         self.bonus = 100
#
#     def calculate_total_bonus(self):
#         return self.salary // 100 * self.bonus
#
#     def __str__(self):  # задает оформление строки вывода
#         return f'CEO {self.name}, salary={self.salary}, bonus={self.bonus}%,' \
#                f' total bonus= {self.calculate_total_bonus()} rub'


if __name__ == '__main__':
    masha = Cleaner('Maria Ivanovna')
    print(masha)
    grisha = Manager('Grigoriy Petrovich')
    print(grisha)
    ivan_palich = CEO('Ivan Pavlovich')
    print(ivan_palich)
