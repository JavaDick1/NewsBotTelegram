# Создание бота и парсер для бота и новостей

from email import message
import telebot;
bot = telebot.TeleBot('5159576994:AAHKFgJ38H0dtAZGms4YrbMjBGADrBwQF9E')

@bot.message_handler(content_types=['start']) ### CHANGE
def get_txt_message(message): # more functionals in START, EJECT
    if message == "Привет":
        bot.send_message(message.from_user.id, "Привет, скоро начну отправлять тебе важные новости")
    elif message == "/help":
        bot.send_message(message.from_user.id, "Для взаимодействия со мной просто напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понял, напиши пожалуйста /help")


bot.polling(none_stop=True,interval=0)

