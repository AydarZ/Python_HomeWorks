# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def input_text():
    return list(input('Ввеедите фразу: ').split())

def find_the_number_of_syllables(text: str):
    count = 0
    for i in text:
        if i in ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я']:
            count += 1
    return count

def rhythm_check(text: list):
    list_with_numbers_of_syllables = list()
    for i in text:
        list_with_numbers_of_syllables.append(find_the_number_of_syllables(i))
    if len(set(list_with_numbers_of_syllables)) == 1:
        print("Парам пам-пам") # если с ритомом всё в порядке
    else:
        print("Пам парам") # если с ритомом не всё в порядке

text = input_text()
rhythm_check(text)