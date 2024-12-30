# Задание: Управление библиотекой книг
def use_book():
    """
    Считает кол-во книг в библиотеке
    :return:
    """
    use_books = 0
    with open('library.txt', 'r', encoding='utf-8') as f:
        for _ in f:
            use_books += 1
    return use_books


def use_book_author(author_name):
    """
    Считает кол-во книг в библиотеке по имени автора
    :return:
    """
    use_books = 0
    with open('library.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if author_name in line:
                use_books += 1
    return use_books


def add_book(book_name, author_name, year):
    """
    Добавляет книгу в библиотеку
    :param book_name: название книги
    :param author_name: имя автора
    :param year: год издания
    """
    try:
        if use_book_author(book_name) == 0:
            with open('library.txt', 'a', encoding='utf-8') as f:
                f.write(f'{book_name};{author_name};{year}\n')
        else:
            print(f'Книга {book_name} уже есть в библиотеке')
    except Exception as e:
        print(f'Ошибка при записи книги: {e}')


def view_books():
    """Выводит все книги в библиотеке"""
    try:
        total_books = use_book()
        with open('library.txt', 'r', encoding='utf-8') as f:
            print(f'=================================Книги в библиотеке:{total_books}=================================')
            for line in f:
                line = line.strip()  # Удаляем пробелы и символы новой строки
                if line:  # Проверяем, что строка непустая
                    book_info = line.split(';')
                    if len(book_info) == 3:  # Проверяем, что есть три элемента
                        print(f'Название: {book_info[0]}\nАвтор: {book_info[1]}\nГод: {book_info[2]}\n')
                    else:
                        print('Неверный формат записи книги:', line)
            print('===================================================================================')
    except FileNotFoundError:
        print('Ошибка открытия файла')


def search_by_author(author_name):
    """Выводит все книги в библиотеке по автору"""
    total_author = use_book_author(author_name)
    try:
        with open('library.txt', 'r', encoding='utf-8') as f:
            found = False
            print(f'Книг данного автора в библиотеке: {total_author}\n')
            for line in f:
                book_info = line.strip().split(';')
                if book_info[1] == author_name:
                    print(f'Название: {book_info[0]}\nГод: {book_info[2]}')
                    found = True
            if not found:
                print('Книг данного автора нет в библиотеке')
    except FileNotFoundError:
        print('Ошибка открытия файла')


def remove_book(book_name):
    """Удаляет книгу из библиотеки"""
    try:
        with open('library.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        with open('library.txt', 'w', encoding='utf-8') as f:
            found = False
            for line in lines:
                if line.startswith(book_name + ";"):
                    found = True
                else:
                    f.write(line)
            if found:
                print('Книга удалена')
            else:
                print('Книга не найдена')
    except FileNotFoundError:
        print('Ошибка открытия файла')


while True:
    choice = input("Что вы хотите сделать? (add/view/search/remove/exit): ").lower()
    if choice == 'add':
        add_book(input("Введите название книги: "),
                 input("Введите имя автора: "),
                 int(input("Введите год издания: ")))
    elif choice == 'view':
        view_books()
    elif choice == 'search':
        search_by_author(input("Введите имя автора: "))
    elif choice == 'remove':
        remove_book(input("Введите название книги: "))
    elif choice == 'exit':
        break
    else:
        print("Неверный ввод, попробуйте еще раз.")
