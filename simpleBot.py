# Бот на Aiogram
# https://surik00.gitbooks.io/aiogram-lessons/content/chapter1.html
from bot_name import bot
import telebot
from telebot import types

token = bot

my_bot = telebot.TeleBot(token)

kb = types.ReplyKeyboardMarkup(row_width=2)
btn1 = types.KeyboardButton('/url')
btn2 = types.KeyboardButton('/flag')
kb.add(btn1, btn2)


@my_bot.message_handler(commands=['start'])
def start_message(message):
    my_bot.send_message(message.chat.id, 'Я запущен.',
                        reply_markup=kb)


@my_bot.message_handler(commands=['help'])
def help_message(message):
    my_bot.send_message(message.chat.id, 'Я пока только Ваше эхо.')


@my_bot.message_handler(commands=['url'])
def url_message(message):
    # inline-keyboard
    markup = types.InlineKeyboardMarkup()
    # Назначаем кнопки
    btn1 = types.InlineKeyboardButton(text='Сайт ИПАП', url='https://ipap.ru')
    btn2 = types.InlineKeyboardButton(text='Сайт Яндекс', url='https://ya.ru')
    # Привязываем кнопки к inline-клавиатуре
    markup.add(btn1, btn2)
    my_bot.send_message(message.chat.id, 'Выберите сайт:',
                        reply_markup=markup)


# Вывод фото
@my_bot.message_handler(commands=['flag'])
def show_flag(message):
    with open('static/images/flag.jpg', 'rb') as flag:
        my_bot.send_photo(message.chat.id, flag, caption='Флаг')


@my_bot.message_handler(content_types=['text'])
def parrot(message):
    if message.text.strip().lower() == 'привет':
        my_bot.send_message(message.chat.id,
                            '<a href="https://mail.ru">MAIL</a>',
                            parse_mode='HTML')
    elif message.text.strip().lower() == 'как дела?':
        # inline-keyboard
        answer = types.InlineKeyboardMarkup(row_width=2)
        # Назначаем кнопки
        btn_good = types.InlineKeyboardButton('Хорошо', callback_data='good')
        btn_bad = types.InlineKeyboardButton('Плохо', callback_data='bad')
        answer.add(btn_good, btn_bad)
        my_bot.send_message(message.chat.id, 'У меня хорошо, а у тебя?',
                            reply_markup=answer)
    else:
        my_bot.send_message(message.chat.id, f'Вы сказали: {message.text}')


@my_bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'bad':
        my_bot.send_message(call.message.chat.id, 'Не переживай 🌞')
    if call.data == 'good':
        my_bot.send_message(call.message.chat.id, 'О! Отлично 😃')


my_bot.infinity_polling(none_stop=True)
