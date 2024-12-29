# Задание 1: Проверка палиндрома
# Описание: Напишите функцию, которая принимает строку и проверяет,
# является ли она палиндромом (читается одинаково как слева направо, так и справа налево).
# Вход: Строка (например, "А роза упала на лапу Азора")
# Выход: Булевое значение (True или False).
def is_palindrome(sting):
    ss = sting.lower().replace(" ", "")
    su = ss == ss[::-1]
    if su:
        return True
    else:
        return False


task1 = is_palindrome('А роза упала на лапу Азора')
print(task1)

task2 = is_palindrome('MADAM')
print(task2)

task3 = is_palindrome('копок')
print(task3)

task3 = is_palindrome('Как раз туда сюда')
print(task3)