from typing import List  # С версии Python 3.9.x импорт не требуется

from typing import Union, Optional, Any


def calc(a: int, b: int) -> int:  # Функция вернет целое число int (и требует аргументов типа int)
    return a + b


# Функция принимает int или float аргументы
def calc_union(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


# Функция принимает int или None аргументы, возвращает любой тип
def calc_optional(a: Optional[int], b: Optional) -> Any:
    return a + b


def to_int(a_list: List[str]) -> list:  # Функция принимает список строк и возвращает список
    return [int(e) for e in a_list]


def to_int_type(a_list) -> List[int]:  # Функция возвращает список, содержащий int (list[int] с версии Python 3.9.x
    return [int(e) for e in a_list]


if __name__ == '__main__':
    print(calc(3, 8))
    print(calc_union(3, 5.1))
    print(calc_optional(9, 4))
    print(to_int(['1', '2', '3', '4', '5', '6']))
    print(to_int_type(['1', '2', '3', '4', '5', '6'])[0])
