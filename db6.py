# Базы данных
# SQL - Structured Query Language
# Структурированный язык запросов
# CRUD - Create Read Update Delete
# Класс для запросов

import sqlite3


class CrudTest:
    def __init__(self, db_name):
        try:
            self.con = sqlite3.connect(db_name)
            self.cur = self.con.cursor()
        except TypeError:
            print('Не указана база данных')

    def read_all(self, table_name):
        res = self.con.execute(f"""
        SELECT * FROM {table_name}
        """).fetchall()
        return res

    def add_genre(self, new_genre):
        try:
            res = self.cur.execute("""SELECT name from genres
            WHERE name = ?""", (new_genre,)).fetchone()
            if res:
                print(f'Жанр "{new_genre}" уже есть в таблице!')
                return
            self.cur.execute(f"""INSERT INTO genres (name)
            VALUES (?)""", (new_genre,))
            self.con.commit()
            print(f'Жанр "{new_genre}" добавлен')
        except Exception as exp:
            print(f'Ошибка при добавлении жанра "{new_genre}"\n {exp}')
            # откат от ошибочной операции
            self.con.rollback()

    def update_genre(self, old_genre, new_genre):
        try:
            self.cur.execute("""UPDATE genres
            SET name = ? WHERE name = ?""",
                             (new_genre, old_genre))
            self.con.commit()
            print(f'Жанр "{old_genre}" обновлен как "{new_genre}"')
        except Exception as exp:
            print(f'Ошибка при обновлении жанра "{old_genre}"\n {exp}')
            # откат от ошибочной операции
            self.con.rollback()

    def delete_genre(self, genre):
        try:
            res = self.cur.execute("""SELECT name from genres
                        WHERE name = ?""", (genre,)).fetchone()
            if not res:
                print(f'Жанр "{genre}" отсутствует в таблице genres!')
                return
            self.cur.execute("""DELETE from genres 
            WHERE name = ?""", (genre,))
            self.con.commit()
            print(f'Жанр "{genre}" удалён.')
        except Exception as exp:
            print(f'Ошибка при удалении жанра "{genre}"\n {exp}')
            # откат от ошибочной операции
            self.con.rollback()

    def __del__(self):
        self.cur.close()
        self.con.close()


crud = CrudTest('db/books_bd.sqlite')

# print(crud.read_all('books'))
crud.delete_genre('Для детей')