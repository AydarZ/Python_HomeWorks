# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def input_number(text: str) -> int:
    return int(input(f'Введите {text}: '))


def fill_array(first, diff, quant) -> list:
    """Заполнение массива элементами арифметической прогрессии"""
    list_result = [first]
    for i in range(2, quant+1):
        list_result.append(first + (i-1)*quant)
    return list_result


first_number = input_number('первый элемент')
difference = input_number('разность')
quantity = input_number('количество элементов')
print(*(fill_array(first_number, difference, quantity)))
