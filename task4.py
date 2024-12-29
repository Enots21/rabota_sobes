# Задание 4: Фильтрация четных чисел
# Описание: Напишите функцию, которая принимает список чисел и возвращает новый список, содержащий только четные числа.
# Вход: Список целых чисел (например, 1, 2, 3, 4, 5)
# Выход: Список четных чисел (например, 2, 4).

def filter_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


result = filter_even_numbers(range(20))
print(result)