# Web-приложение
# SOA - Service Oriented Architecture
# MSA - Micro Service Architecture
# REST - REpresentational State Transfer
# Читаем все новости через API v2

import datetime
import os

from flask import (Flask, request, render_template,
                   redirect, abort, make_response, jsonify)
import sqlite3
from flask_restful import Api

from dotenv import load_dotenv
from flask_mail import Mail, Message
from data import db_session
from data.news import News
from data.users import User
import requests as r
from data.news_api import blueprint
from data import api_resources
from forms.loginform import LoginForm
from forms.feedback_form import MailForm
from forms.news import NewsForm
from forms.town import TownForm
from forms.user import RegisterForm
from flask_login import (LoginManager, login_user, logout_user,
                         login_required, current_user)

load_dotenv()  # Загружаем переменные окружения перед созданием приложения

app = Flask(__name__)
api = Api(app)  # для подключения ресурсов к приложению
app.config['SECRET_KEY'] = 'just_simple_key'
# Время жизни сессий для данного приложения
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)

# Конфигурация для почты
app.config.update(
    MAIL_SERVER=os.environ.get('HOST'),
    MAIL_PORT=os.environ.get('PORT'),
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=os.environ.get('FROM'),
    MAIL_PASSWORD=os.environ.get('PASSWORD'),
    MAIL_DEFAULT_SENDER=os.environ.get('FROM')
)

mail = Mail(app)


def send_mail(subject, message, recipient=None):
    if not app.config.get('MAIL_SERVER') or not app.config.get('MAIL_PASSWORD'):
        return 'Почта не настроена'

    try:
        recipient = recipient or ['wmast@inbox.ru']

        msg = Message(
            subject=subject,
            sender=app.config.get('MAIL_DEFAULT_SENDER', 'noreply@nodomen.ru'),
            recipients=recipient)

        msg.body = message
        mail.send(msg)  # отправка
        return f'Письмо успешно отправлено на адрес: {','.join(recipient)}!'
    except Exception as e:
        app.logger.error(f'Ошибка: {e}')
        return 'Ошибка при отправке'


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)


@app.errorhandler(401)
def unauthorized(error):
    return redirect('/login')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Новость не найдена'}), 404)


@app.errorhandler(400)
def not_found(_):
    return make_response(jsonify({'error': 'Некорректный запрос'}), 400)


@app.route('/')  # декоратор
@app.route('/home')
@login_required
def index():
    params = {
        'user': 'слушатель от ИПАП',
        'title': 'Пример рендеринга',
        'active_page': 'home'
    }
    return render_template('index.html', **params)
    # return render_template('index.html',
    # user='слушатель от ИПАП',
    # title='Пример рендеринга')


@app.route('/contacts', methods=['GET', 'POST'])
def feedback():
    form = MailForm()
    if form.validate_on_submit():
        m = (f'Пользователь с адресом: {form.email.data} отправил Вам:\n'
             f'{form.mess.data}')
        res = send_mail('Сообщение с сайта,', m)
        return render_template('feedback.html',
                               title='Результат отправки',
                               active_page='contacts',
                               form=form,
                               message=res)
    return render_template('feedback.html',
                           title='Обратная связь', form=form,
                           active_page='contacts')


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    form = TownForm()
    if form.validate_on_submit():
        town = form.town.data
        if town:
            params = {
                'q': town,
                'lang': 'ru',
                'units': 'metric',
                'appid': 'Ваш ключ'
            }
            temp = r.get('https://api.openweathermap.org/data/2.5/weather',
                         params=params)
            res = temp.json()
            if res['cod'] == 200:
                result = {'title': f'Погода в городе {town}', 'temper': res['main']['temp'],
                          'humidity': res['main']['humidity'], 'pressure': res['main']['pressure']}
                return render_template('get_weather.html', **result)
            else:
                return render_template('get_weather.html',
                                       title='Город не найден')
        else:
            abort(404)
    return render_template('weather.html',
                           title='Погода', form=form, active_page='weather')


# Через Web-интерфейс
# @app.route('/news')
# def all_news():
#     db_sess = db_session.create_session()
#     # Выведем либо все публичные новости, либо все новости для автора
#     if current_user.is_authenticated:
#         all_news = db_sess.query(News).filter(
#             (News.user == current_user) | (News.is_private != True)).all()
#     else:
#         all_news = db_sess.query(News).filter(
#             News.is_private != True).all()
#     return render_template('news.html',
#                            title='Список новостей',
#                            news=all_news)

# Через API (все новости, без ограничений)
@app.route('/news')
def all_news():
    news = r.get('http://127.0.0.1:5000/api/news').json()
    return render_template('news_api.html',
                           title='Новости через API',
                           news=news['news'], active_page='news')


@app.route('/news/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = NewsForm()
    if request.method == 'GET':
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(
            News.id == id,
            News.user == current_user
        ).first()
        if news:
            form.title.data = news.title
            form.content.data = news.content
            form.is_private.data = news.is_private
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(
            News.id == id,
            News.user == current_user
        ).first()
        if news:
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            news.created_date = datetime.datetime.now()
            db_sess.commit()
            return redirect('/news')
        else:
            abort(404)
    return render_template('add_news.html',
                           title='Редактирование новости',
                           form=form, active_page='news')


@app.route('/add_news', methods=['GET', 'POST'])
@login_required
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        current_user.news.append(news)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/news')
    return render_template("add_news.html",
                           title="Добавление новости", form=form)


@app.route('/news_del/<int:id>')
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(
        News.id == id,
        News.user == current_user
    ).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/news')


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


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/home')


@app.route('/conditions-sample/<int:number>')
def even_odd(number):
    return render_template('even_odd.html',
                           number=number,
                           title='Чётное или нечётное')


@app.route('/about')  # декоратор
def about():
    return render_template('about.html',
                           title='Про нас',
                           active_page='about')


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
    # app.register_blueprint(blueprint)  # зарегистрировали Blueprint
    # уже не Blueprint, а ресурсы от flask-restful
    api.add_resource(api_resources.NewsResourceList, '/api/news')
    api.add_resource(api_resources.NewsResourse, '/api/news/<int:news_id>')
    app.run(host='127.0.0.1', port=5000, debug=True)
