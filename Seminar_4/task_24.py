# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены 
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте 
# выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит 
# из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно 
# перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном списке содержащим количество ягод на кустах.

from random import randint


n = int(input('Введите количество кустов на грядке: '))
list_berries = [randint(0,20) for i in range(n)]
print(*list_berries)
list_berries_from3 = []

for i in range(len(list_berries)-1):
    list_berries_from3.append(list_berries[i] + list_berries[i+1] + list_berries[i-1])
list_berries_from3.append(list_berries[0] + list_berries[-2] + list_berries[-1])

print('Максимально можно собрать за один раз ягод: ', max(list_berries_from3))


