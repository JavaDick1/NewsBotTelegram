# Создание бота и парсер для бота и новостей
from email import message
from lib2to3.pgen2 import token
import telebot;
token = "5159576994:AAHKFgJ38H0dtAZGms4YrbMjBGADrBwQF9E"
id_channel = "1432747261"
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text']) ### CHANGE
def get_txt_message(message): # more functionals in START, EJECT
    bot.send_message(id_channel, message.text)


bot.polling(none_stop=True)

