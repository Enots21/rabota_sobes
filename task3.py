# Задание 3: Факториал
# Описание: Напишите функцию, которая рассчитывает факториал числа.
# Вход: Целое число n (например, 5)
# Выход: Целое число — факториал n (например, 120 для 5).

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)
print(result)

result = factorial(10)
print(result)

result = factorial(15)
print(result)