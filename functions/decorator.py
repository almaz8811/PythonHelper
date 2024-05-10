# Внутренняя функция может захватывать переменные из внешней

def logger(func):
    def wrapper(a, b):
        print(f'{func.__name__} started')
        result = func(a, b)
        print(f'{func.__name__} finished')
        return result

    return wrapper


@logger
def summ(a, b): # в этот момент summ=wrapper
    return a + b


if __name__ == '__main__':
    # function = logger(summ)
    # print(function)
    print(summ(2, 3))
