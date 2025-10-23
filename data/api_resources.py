# REST API, версия 2
# Работаем не на уровне отдельных функций
# а на уровне ресурсов
from flask import jsonify
from flask_restful import abort, Resource, reqparse

from data import db_session
from data.news import News


# Прерываем выполнение, если ресурс не найден
def abort_if_news_not_found(news_id):
    db_sess = db_session.create_session()
    news = db_sess.get(News, news_id)
    if not news:
        abort(404, error=f'Новость с id={news_id} не найдена!')


# Ресурс, читающий отдельную новость
# и удаляющий новость с id
class NewsResourse(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        db_sess = db_session.create_session()
        news = db_sess.get(News, news_id)
        return jsonify(
            {
                'news': news.to_dict(
                    only=('title', 'content', 'user_id', 'is_private')
                )

            }
        )

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        db_sess = db_session.create_session()
        news = db_sess.get(News, news_id)
        db_sess.delete(news)
        db_sess.commit()
        return jsonify({'success': f'Новость {news_id} удалена'})


# Тут пропишем parser
parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('content', required=True)
parser.add_argument('is_private', required=True, type=bool)
parser.add_argument('user_id', required=True, type=int)


# Ресурс, читающий все новости
class NewsResourceList(Resource):
    def get(self):
        db_sess = db_session.create_session()
        news = db_sess.query(News).all()
        if not news:
            return jsonify({'error': 'Новостей нет'})
        return jsonify(
            {
                'news': [item.to_dict(
                    only=('title', 'content', 'user.name')
                )
                    for item in news]
            }
        )

    def post(self):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        news = News(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id'],
            is_private=args['is_private']
        )
        db_sess.add(news)
        db_sess.commit()
        return jsonify({'id': news.id})
