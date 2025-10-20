# Blueprint ("синька") для API
import flask


blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/news')
def get_news():
    return 'Соответствующий обработчик API'
