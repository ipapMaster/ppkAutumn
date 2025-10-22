from flask_wtf import FlaskForm
from wtforms import EmailField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class MailForm(FlaskForm):
    email = EmailField('Ваша почта:',
                       validators=[
                           DataRequired('Введите почту'),
                           Email('E-mail некорректен'),
                           Length(min=3, max=50,
                                  message='Почта должен быть не менее 3 и не более 50 символов ')])
    mess = TextAreaField('Ваше сообщение:',
                         validators=[
                             DataRequired('Введите текст сообщения'),
                             Length(min=3, max=250,
                                    message='Текст сообщения должен быть не менее 3 и не более 250 символов ')])
    submit = SubmitField('Отправить')
