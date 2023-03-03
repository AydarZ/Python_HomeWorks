# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую неотрицательную степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def input_number(text: str) -> int:
    return int(input(f'Введите {text}: '))


def exponentiation_rec(a: int, b: int) -> int:
    if b == 0:
        return 1
    return a * exponentiation_rec(a, b-1)


a = input_number('A')
b = input_number('B (неотрицательное)')
print(exponentiation_rec(a, b))
