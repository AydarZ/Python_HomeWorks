# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
#  4


def input_number(text: str) -> int:
    return int(input(f'Введите {text}: '))


def summ_rec(a: int, b: int, i=-1) -> int:
    if i == b:
        return b
    else:
        return a + summ_rec(0, b, i+1)


a = input_number('A')
b = input_number('B')
print(summ_rec(a, b))
