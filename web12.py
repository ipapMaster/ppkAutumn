# Web-приложение
# Flask - SQLAlchemy - Object Relational Mapping (ORM)
# Объектно-реляционное отображение (авторизация)
import datetime

from flask import Flask, request, render_template, redirect
import sqlite3
from data import db_session
from data.news import News
from data.users import User
from forms.loginform import LoginForm
from forms.user import RegisterForm
from flask_login import LoginManager, login_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'just_simple_key'
# Время жизни сессий для данного приложения
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


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


# @app.route('/cookie_test')
# def cookie():
#     visit_count = int(request.cookies.get('visit_count', 0))
#
#     if visit_count:
#         res = make_response(
#             f'Вы посетили данную страницу {visit_count + 1} раз'
#         )
#         res.set_cookie('visit_count', str(visit_count + 1),
#                        max_age=60 * 60 * 24 * 365)  # установил cookie на 1 год
#
#     else:
#         res = make_response('Вы пришли на эту страницу 1 раз за последний год')
#         res.set_cookie('visit_count', '1',
#                        max_age=60 * 60 * 24 * 365)
#     return res

# @app.route('/session_test')
# def sess_test():
#     visit_count = session.get('visit_count', 0)
#
#     session['visit_count'] = visit_count + 1
#     return make_response(
#         f'Вы посетили данную страницу {visit_count + 1} раз.'
#     )


@app.route('/news')
def all_news():
    db_sess = db_session.create_session()
    # Выведем все публичные новости
    all_news = db_sess.query(News).filter(News.is_private != True).all()
    return render_template('news.html',
                           title='Список новостей',
                           news=all_news)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():  # Это работает метод POST
        if form.password.data != form.password_again.data:
            return render_template('register.html',
                                   title='Пароли не совпали',
                                   message='Пароли не совпадают',
                                   form=form)
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html',
                                   title='Пользователь существует',
                                   message='Такой пользователь уже есть в базе',
                                   form=form)
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    # а если метод GET
    return render_template('register.html',
                           title='Регистрация',
                           form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/news')
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
    db_session.global_init('db/blogs.db')
    app.run(host='127.0.0.1', port=5000)
