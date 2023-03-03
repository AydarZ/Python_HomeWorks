# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# def fibonachchi (n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonachchi(n-1) + fibonachchi(n-2)

# n = int(input('Введите число N: '))
# print('N-е число Фибоначчи: ', fibonachchi(n-1))

# list_fib = []
# for i in range(n):
#     list_fib.append(fibonachchi(i))
# print(*list_fib)




# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

list_journal = list(map(int, input("Введите оценки через пробел: ").split()))
minimal = min(list_journal)
maximal = max(list_journal)
for i in range(len(list_journal)):
    if list_journal[i] == maximal:
        list_journal[i] = minimal

print(*list_journal)
