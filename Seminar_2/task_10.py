# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input("Введите количество монет "))
string_values = ""
count_1 = 0
count_0 = 0
for i in range(n):
    value = random.randint(0, 1)
    print(value, end=' ')
    string_values += str(value)
print()
for i in range(len(string_values)):
    if string_values[i] == "1":
        count_1 += 1
    else:
        count_0 += 1
if count_0 > count_1:
    print(count_1)
else:
    print(count_0)
