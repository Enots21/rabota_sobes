#  Удаление дубликатов
# Описание: Напишите функцию, которая принимает список и удаляет все дубликаты, оставляя уникальные значения.
# Вход: Список (например, 1, 2, 2, 3, 4, 4, 5)
# Выход: Список уникальных значений (например, 1, 2, 3, 4, 5).

def remove_duplicates(list):
    return set(list)

print(list(remove_duplicates([1, 2, 2, 3, 4, 4, 5])))
print(list(remove_duplicates([1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9])))
