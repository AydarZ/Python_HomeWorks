# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# print ("Введите трёхзначное число")
# a = int(input())
# summ = 0
# while a > 0:
#     x = a % 10
#     summ += x
#     a //= 10
# print('сумма чисел равна: ', summ)



# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# print ("Введите число журавликов S:")
# s = int(input())
# if s % 6 == 0:
#     a = s//6    
#     b = (a+a)*2
#     print(a, b, a)
# else:
#     print ('неверное S')



# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# print ("Введите шестизначный номер билета:")
# s = int(input())
# first_num = s // 1000
# summ_first = 0
# while first_num > 0:
#     x = first_num % 10
#     summ_first += x
#     first_num //= 10

# second_num = s % 1000
# summ_second = 0
# while second_num > 0:
#     x = second_num % 10
#     summ_second += x
#     second_num //= 10

# if summ_first == summ_second:
#     print('yes')
# else:
#     print ('no')



# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

# n = int(input("Введите число n:"))
# m = int(input("Введите число m:"))
# k = int(input("Введите число k:"))

# if  (k < n*m) and (k % n == 0 or k % m == 0):
#     print('yes')
# else:
#     print("no")
