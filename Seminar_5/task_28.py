# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
#  4


def input_number(text: str) -> int:
    return int(input(f'Введите {text}: '))

def summ_rec(a: int, b:int) -> int:
    if a == 0:
        return b
    return summ_rec(a-1, b+1)


a = input_number('A')
b = input_number('B')
print(summ_rec(a, b))
