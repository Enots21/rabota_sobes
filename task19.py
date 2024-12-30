# Чтение и запись файла:
# Напишите программу, которая считывает содержимое текстового файла и записывает его в новый файл
# в верхнем регистре. Если исходный файл не существует, программа должна вывести сообщение об ошибке.

def int_main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            text = f.read()
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(text.upper())
    except FileNotFoundError:
        print('Файл не найден')

int_main()