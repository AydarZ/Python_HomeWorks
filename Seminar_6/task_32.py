# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint


def create_random_list(length) -> list:
    return [randint(-20, 20) for i in range(length)]

def input_number(text: str) -> int:
    return int(input(f'Введите {text}: '))

def find_indexes_of_elements_for_diapazon(lst, min, max) -> list:
    list_indexes = []
    for i in range(len(lst)):
        if min <= lst[i] <= max:
            list_indexes.append(i)
    return list_indexes


array = create_random_list(10)
print (array)
minimal = input_number('минимум')
maximal = input_number('максимум')
print(find_indexes_of_elements_for_diapazon(array, minimal, maximal))