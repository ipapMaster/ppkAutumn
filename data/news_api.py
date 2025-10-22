# Blueprint ("синька") для API
import flask
from flask import jsonify, make_response, request
from . import db_session
from .news import News
import datetime

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


# Получить все новости методом GET
@blueprint.route('/api/news')
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(News).all()
    return jsonify(
        {
            'news':
                [item.to_dict(only=('title',
                                    'content',
                                    'user.name',
                                    'created_date'))
                 for item in news]
        }
    )


# Получить одну новость по ID
@blueprint.route('/api/news/<int:news_id>', methods=['GET'])
def get_one_news(news_id):
    db_sess = db_session.create_session()
    news = db_sess.get(News, news_id)
    if not news:
        return make_response(jsonify({'error': f'Новость с ID: {news_id} не найдена.'}))
    return jsonify(
        {
            'news': news.to_dict(only=('title', 'content', 'user_id', 'is_private'))
        }
    )


# Добавление новости
@blueprint.route('/api/news', methods=['POST'])
def create_news():
    if not request.json:
        return make_response(jsonify({'error': 'Пустой запрос'}), 400)
    elif not all(key in request.json for key in ['title', 'content', 'user_id', 'is_private']):
        return make_response(jsonify({'error': 'Некорректный запрос'}), 400)
    db_sess = db_session.create_session()
    news = News(
        title=request.json['title'],
        content=request.json['content'],
        user_id=request.json['user_id'],
        is_private=request.json['is_private']
    )
    db_sess.add(news)
    db_sess.commit()
    return jsonify({'id': news.id})


# Изменение новости: полное (PUT) или частичное (PATCH)
@blueprint.route('/api/news/<int:news_id>', methods=['PUT', 'PATCH'])
def edit_news(news_id):
    if not request.json:
        return make_response(jsonify({'error': 'Пустой запрос'}), 400)
    db_sess = db_session.create_session()
    news = db_sess.get(News, news_id)
    if not news:
        return make_response(jsonify({'error': 'Новость отсутствует'}), 404)
    # Список полей под редактирование (разрешённых)
    allowed_fields = {'title', 'content', 'user_id', 'is_private'}
    if request.method == 'PUT':  # редактируем все поля
        if not all(field in request.json for field in allowed_fields):
            return make_response(jsonify({'error': 'Некорректный запрос'}), 400)
    # Обновляем только те поля, которые были переданы
    for key, value in request.json.items():
        if key in allowed_fields:
            setattr(news, key, value)
    db_sess.commit()
    return jsonify({'success': f'Поля новости {news.title} заменены.'})


# Удаление новости
@blueprint.route('/api/news/<int:news_id>', methods=['DELETE'])
def delete_news(news_id):
    db_sess = db_session.create_session()
    news = db_sess.get(News, news_id)
    if not news:
        return make_response(jsonify({'error': f'Новости с id {news_id} нет в БД. Нечего удалять!'}))
    db_sess.delete(news)
    db_sess.commit()
    return jsonify({'success': f'Новость "{news.title}" удалена!'})
