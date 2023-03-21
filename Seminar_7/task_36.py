# Задача 36: На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран получившийся кортеж.
# Sample Input:
# house=дом car=машина men=человек tree=дерево
# Sample Output:
# ((house, дом), (car, машина), (men, человек), (tree, дерево))

def input_text():
    return tuple(input('Ввеедите строку: ').split())

def split_the_word(word):
    for i in range(len(word)):
        if word[i] == '=':
            return (word[:i], word[i+1:len(word)])
        
print(tuple(map(split_the_word, input_text())))
