# Web-приложение
# Flask - минимализм, с возможностью расширения
# устанавливаем pip install flask
# Django - всё включено (не используем)
from flask import Flask, url_for
import sqlite3

app = Flask(__name__)


@app.route('/')  # декоратор
@app.route('/home')
def index():
    return """Я Ваше первое приложение.
    <br>Подробнее <a href="/about">здесь</a>
    <br>А вот <a href="/countdown">тут</a> обратный отсчёт"""


@app.route('/about')  # декоратор
def about():
    return """Это страница с более подробной информацией.
    <br>А <a href="/genres">тут</a> про жанры.
    <br>А <a href="/flag">тут</a> будет флаг.
    <br><a href="/home">Назад</a>"""


@app.route('/countdown')
def cdown():
    lst = [str(x) for x in reversed(range(11))]
    lst.append('Поехали!!!')
    return '<br>'.join(lst)


@app.route('/genres')
def genres():
    temp = []
    con = sqlite3.connect('db/books_bd.sqlite')
    cur = con.cursor()
    res = cur.execute("SELECT * FROM genres").fetchall()
    cur.close()
    con.close()
    for _, name in res:
        temp.append(name)
    temp = list(map(lambda x: '<li>' + x + '</li>', temp))
    res = '<br>'.join(temp)
    result = f"""
    <!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{url_for('static', filename='css/styles.css')}">
    <title>Жанры</title>
</head>
<body>
<h1>А вот и жанры:</h1>
<ul>
{res}
</ul>
</body>
</html>
    """
    return result


@app.route('/flag')
def flag():
    return f"""<img src="{url_for('static', filename='images/flag.jpg')}" 
    height="40" width="60" 
    alt="Нету флага">"""


# <name> - строка
# <num:int> - целое
# <num:float> - дес. дробь
@app.route('/greet', defaults={'name': None})
@app.route('/greet/<name>')
def greeting(name=None):
    if name is None:
        return '<h1>Не с кем здороваться!!!</h1>'
    return f"""
    <!DOCTYPE html>
<html lang="ru">
<head>
<!--    как будет отображаться на странице-->
    <meta charset="UTF-8">
    <meta name="description" content="Описание страницы сайта.">
    <link rel="stylesheet" href="{url_for('static', filename='css/styles.css')}">
    <title>Приветствуем тебя, {name}</title>
</head>
<body>
<h1>{name.capitalize()}, мы приветствуем тебя</h1>
</body>
</html>
    """


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
