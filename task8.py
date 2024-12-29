# Задание 8: Ошибка в списке
# Описание: Напишите функцию, которая принимает список целых чисел от 1 до n,
# но одно число отсутствует. Найдите это число.
# Вход: Список целых чисел (например, 1, 2, 4, 5, n=5)
# Выход: Отсутствующее число (например, 3).

def find_missing_number(numbers: list, n: int) -> int:
    for number in numbers:  # Проверка на вхождение чисел в списке
        if number not in range(1, n + 1):  # Проверка на вхождение чисел в списке
            raise ValueError('Number is out of range')
    if len(numbers) != n - 1:  # Проверка на вхождение чисел в списке
        raise ValueError('List is not correct')  # Проверка на вхождение чисел в списке
    for number in range(1, n + 1):  # Проверка на вхождение чисел в списке
        if number not in numbers:  # Проверка на вхождение чисел в списке
            return number  # Проверка на вхождение чисел в списке


result = find_missing_number([1, 2, 4, 5], 5)
print(result)

result = find_missing_number([1, 2, 4, 5, 6], 6)
print(result)
