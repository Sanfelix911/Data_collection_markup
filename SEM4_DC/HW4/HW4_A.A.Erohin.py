
import requests
from lxml import html
from pymongo import MongoClient

# Парсим страницу портала GB с каталогом курсов по Пайтону (скрин HW4_1) https://gb.ru/courses/programming
# Берем User-Agent (скрин HW4_2)

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

url = 'https://gb.ru'
response = requests.get(url +'/courses/programming' , headers=header)
print(response) # получили 200
dom = html.fromstring(response.text)

# Название курса
course_name = dom.xpath("//span[@class = 'direction-card__title-text ui-text-body--1 ui-text--medium']/text()")
# Срок обучения
term_training = dom.xpath("//div[1]/span[@class = 'ui-text--medium']/text()")
# скидка на обучение
discount = dom.xpath("//div[@class = 'direction-card__info-label ui-text-heading--5 ui-text--medium gb-landings-product-discount']/text()")
print(discount)




