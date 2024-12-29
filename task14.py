# Описание: Напишите функцию, которая принимает строку и возвращает её, где слова упорядочены по их длине.
# Вход: Строка (например, "the quick brown fox")
# Выход: Строка с упорядоченными словами (например, "the fox quick brown").


def task13(string):
    string = string.split()  # делим строку на слова
    string.sort(key=len)  # сортируем слова по длине
    return ' '.join(string)  # переводим слова в строку


print(task13("the quick brown fox"))
