# Web-приложение
# Flask - работаем с шаблонами
from flask import Flask, url_for, request, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')  # декоратор
@app.route('/home')
def index():
    params = {
        'user': 'слушатель от ИПАП',
        'title': 'Пример рендеринга'
    }
    return render_template('index.html', **params)
    # return render_template('index.html',
    # user='слушатель от ИПАП',
    # title='Пример рендеринга')


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


@app.route('/form-sample', methods=['GET', 'POST'])
def form_sample():
    if request.method == 'GET':
        return render_template('form_sample.html',
                               form_title='Форма для регистрации')
    elif request.method == 'POST':
        m = request.form.get('email')
        password = request.form.get('password')
        genderSelect = request.form.get('genderSelect')
        gender = 'мужской' if genderSelect == 'М' else 'женский'
        ab = request.form.get('about')
        remember = request.form.get('remember')
        if remember == 'on':
            st = 'запомнить'
        else:
            st = 'не запоминать'
        return render_template('result.html',
                               title='Результат отправки',
                               email=m, password=password,
                               gender=gender, about=ab, status=st)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
