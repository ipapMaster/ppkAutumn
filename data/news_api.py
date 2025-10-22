# Blueprint ("синька") для API
import flask
from flask import jsonify, make_response
from . import db_session
from .news import News

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
                [item.to_dict(only=('title', 'content', 'user.name'))
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
