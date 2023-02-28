# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n) самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. Последняя строка содержит число X

from random import randint

n = int(input('Введите количество элементов в массиве: '))
list_1 = [randint(1, 50) for i in range(n)]
print(*list_1)
x = int(input('Введите число X: '))
difference = 49 # так как рандомим от 1 до 50ти
for i in list_1:
    temp = abs(i - x)
    if temp < difference:
        difference = temp
        result = i
print(result)