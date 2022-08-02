import wikiModel, telebot
import random


# Создаем экземпляр бота
bot = telebot.TeleBot('5366147447:AAHszjrtM0bHWKALS_2mVTWQIZOb6SpxIpA')
# keys = telebot.types.ReplyKeyboardMarkup(True, True)

# keys.row('Русский', 'Английский')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    bot.send_message(message.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')


# @bot.message_handler(commands=["lang"])
# def chooseLang(message):
#     bot.send_message(message.chat.id, 'Выбери язык запроса:', reply_markup=keys)
#     wikiModel.set_lang(message.text)
#     message.text = None

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, random.choice(['Ищу информацию...', 'Поиск...', 'Проходимся по википедии...']))
    bot.send_message(message.chat.id, wikiModel.getwiki(message.text)[0] + wikiModel.getwiki(message.text)[1])

# Запускаем бота
bot.polling(none_stop=True, interval=0)