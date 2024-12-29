# **Поиск максимального и минимального элемента в списке:**
#    - Напишите функцию, которая принимает список чисел и возвращает кортеж,
#    содержащий минимальное и максимальное значения. Не используйте встроенные функции `max` и `min`.


def find_max_min(numbers):
    max_number = numbers[0]  # максимальное число
    min_number = numbers[0]  # минимальное число
    for number in numbers:  # цикл по списку
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number
    return min_number, max_number


print(find_max_min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
