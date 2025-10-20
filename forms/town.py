from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class TownForm(FlaskForm):
    town = StringField('Город:',
                       validators=[
                           DataRequired('Нужно ввести название города'),
                           Length(min=3, max=50,
                                  message='Название должно быть не менее 3 и не более 50 символов ')])
    submit = SubmitField('Получить')
