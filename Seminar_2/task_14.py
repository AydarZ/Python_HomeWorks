# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.

n = int(input('Введите число N '))
num = 1
k = 0

while num < n:
    print (num, end=' ')
    k +=1
    num = 2**k
    