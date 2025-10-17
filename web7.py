# Web-приложение
# Flask - работаем с формами через flask-wtf
from flask import Flask, request, render_template
import sqlite3

from forms.loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'just_simple_key'


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Успех'
    return render_template('login.html',
                           title='Авторизация',
                           f=form)


@app.route('/conditions-sample/<int:number>')
def even_odd(number):
    return render_template('even_odd.html',
                           number=number,
                           title='Чётное или нечётное')


@app.route('/about')  # декоратор
def about():
    return render_template('about.html', title='Про нас')


@app.route('/countdown')
def cdown():
    lst = [str(x) for x in reversed(range(11))]
    lst.append('Поехали!!!')
    return render_template('countdown.html',
                           title='Обратный отсчёт',
                           array=lst)


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
    return render_template('genres.html',
                           title='Жанры',
                           array=temp)


@app.route('/flag')
def flag():
    return render_template('flag.html', title='Флаг')


# <name> - строка
# <num:int> - целое
# <num:float> - дес. дробь
@app.route('/greet', defaults={'name': None})
@app.route('/greet/<name>')
def greeting(name=None):
    if name is None:
        return render_template('greet.html',
                               title='Приветствие',
                               text='Не с кем здороваться!!!')
    return render_template('greet.html',
                           title=f'Приветствуем, {name.capitalize()}!',
                           text=f'{name.capitalize()}, мы приветствуем тебя')


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
