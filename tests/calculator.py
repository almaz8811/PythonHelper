# Написать функцию calculator, которая принимает на фход строку, содержащую два целых числа и один знак арифметической
# операции + - * / и возвращает результат выполнения этой операции. Если числа не целые или нет знака операции, то
# бросать исключение ValueError.

def calculator(expresssion):
    allowed = '+-*/'
    if not any(sign in expresssion for sign in allowed):
        raise ValueError(f'Выражение должно содержать хотя бы один знак ({allowed})')
    for sign in allowed:
        if sign in expresssion:
            try:
                left, right = expresssion.split(sign)
                left, right = int(left), int(right)
                if sign == '+':
                    return left + right
                elif sign == '-':
                    return left - right
                elif sign == '*':
                    return left * right
                elif sign == '/':
                    return left / right
            except (ValueError, TypeError):
                raise ValueError(f'Выражение должно содержать 2 целых числа и один знак')

if __name__ == '__main__':
    print(calculator('1 + 2'))
