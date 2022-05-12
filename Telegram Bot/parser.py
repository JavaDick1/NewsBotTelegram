# New api and Parser
import requests
from bs4 import BeautifulSoup
from yarl import URL

URL = "https://riamo.ru/tag/743/moskva-reka-xl"

page = requests.get(URL)
soup = BeautifulSoup(page.content,"html.parser")

post = soup.findAll("a", class_="card_horizontal--img-container")

title = post.findAll("a", class_= "card_horizontal__header").text.strip()
description = post.findAll("div", class_= "card_horizontal__description").text.strip()
url = post.findAll("a", class_="card_horizontal__img-container", href=True)["href"].strip()


print(title, description, url, sep="\n\n")