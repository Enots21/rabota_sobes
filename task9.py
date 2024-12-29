# Задание 9: Классификация чисел
# Описание: Напишите функцию, которая принимает список чисел и возвращает два списка:
# один с четными и другой с нечетными числами.
# Вход: Список целых чисел (например, 1, 2, 3, 4, 5)
# Выход: Два списка (например, (2, 4, 1, 3, 5)).


def classify_numbers(numbers: list) -> tuple:
    even_numbers = []
    odd_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    return even_numbers, odd_numbers

print(classify_numbers([1, 2, 3, 4, 5]))
print(classify_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
