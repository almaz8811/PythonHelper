# dunder дандер, магический метод
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f'{self.name} says Meow!')

    def __add__(self, other):  # метод сложения объектов
        if isinstance(other, Cat):
            return Cat('Ginget', 0)


if __name__ == '__main__':
    tom = Cat('Tom', 2)
    angela = Cat('angela', 1)
    print(tom)
    print(angela)
    tom.meow()
    angela.meow()
    ginger = tom + angela
    ginger.meow()
