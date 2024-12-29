# **Генерация паролей:**
#    - Напишите программу, которая генерирует случайные пароли заданной длины,
# используя буквы верхнего и нижнего регистра, цифры и специальные символы.

import random

def password():
    password = ''
    for i in range(50):
        password += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+')
    return password
print(password())