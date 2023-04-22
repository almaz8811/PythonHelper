# Полиморфизм - это механизм, позволяющий выполнять один и тот же код по-разному
# Ducktyping (утиная типизация) - наличие поведения для использования в полиморфизме
# В ЯП со статической типизацией для полиморфизма важно кто ты (какой тип), для Python важно что ты умеешь (повоедение)
class Animal:
    def make_noise(self):
        print('shh')


class Cat(Animal):
    def make_noise(self):
        print('meow')


class Dog(Animal):
    def make_noise(self):
        print('gavv')


class Car:
    def make_noise(self):
        print('bi-bi')


def noise(animal: Animal):
    animal.make_noise()


################################################################
class SQLiteDatabase:
    def connect(self):
        print('Connecting to database SQLiteDatabase')

    def get_users(self):
        print('Getting users SQL')


class MongoDatabase:
    def connect(self):
        print('Connecting to database MongoDatabase')

    def get_users(self):
        print('Getting users noSQL')


class Server:
    def get_users(self, db):
        # db = SQLiteDatabase()
        db.connect()
        users = db.get_users()
        return users


if __name__ == '__main__':
    boby = Dog()
    noise(boby)
    noise(Car())
    ################################################################
    server = Server()
    server.get_users(MongoDatabase())
