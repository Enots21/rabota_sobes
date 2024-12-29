# - Создайте функцию, которая принимает строку и возвращает её,
# перевернутую задом наперед. При этом не используйте встроенные функции для реверса.

def reverse(string):
    new_string = ''  # Создайте новую переменную, в которую запишите строку,
    for i in range(len(string)-1, -1, -1):  #Цикл для перевернутой строки
        new_string += string[i]  #Добавьте каждый символ в новую переменную
    return new_string

print(reverse('hello'))
print(reverse('world'))
print(reverse('python'))