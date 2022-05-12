import telebot
from bs4 import BeautifulSoup
import requests
bot = telebot.TeleBot("5159576994:AAHKFgJ38H0dtAZGms4YrbMjBGADrBwQF9E")
url = 'https://riamo.ru/tag/743/moskva-reka-xl'
page = requests.get(url)
 
# Парсим страницу
 
soup = BeautifulSoup(page.text, 'html.parser')
events = soup.find("a", class_="card-horizontal--img-container")
print(events)
 
# Собираем необходимые данные со страницы:
 
answer = ''
for i in events:
  event = i.find('section').find('h2').find('a').get_text()
  try:
      desc = i.find('section').find('div', class_='').get_text()
  except:
      desc = "Нет описания"
  date = i.find('section').find('div', class_='card-horizontal--img-container').get_text()
 
  answer += event + desc + date + '\n\n'
 
print(answer)
# Отправляем через бота:
 
@bot.message_handler(content_types=['text'])
def send_events_chel(message):
    bot.send_message(message.chat.id, answer)
    bot.polling(none_stop=True)