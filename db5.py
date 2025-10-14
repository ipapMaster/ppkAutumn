# Базы данных
# SQL - Structured Query Language
# Структурированный язык запросов
# CRUD - Create Read Update Delete
# % - набор любых символов от None до ...
# _ - один любой символ
import sqlite3

# Подключиться к БД
with sqlite3.connect('db/books_bd.sqlite') as con:

    # Создание курсора
    cur = con.cursor()

    # Корректно использовать защищённый параметризированный запрос
    result = cur.execute(
        """SELECT title, author FROM books 
    WHERE year BETWEEN ? AND ?""", (1970, 1980)
    ).fetchmany(3)

    print('С 1970 по 1980 в библиотеке книг:', len(result))

    for num, (title, author) in enumerate(result):
        print(f'{num + 1}. Автор: {author}\tНазвание: {title}')

    # Выключаем курсор
    cur.close()

