
import requests
from lxml import html


# Парсим страницу портала GB с каталогом курсов по Пайтону (скрин HW4_1) https://gb.ru/courses/programming
# Берем User-Agent (скрин HW4_2)

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

url = 'https://gb.ru'
response = requests.get(url +'/courses/programming' , headers=header)
print(response) # получили 200
dom = html.fromstring(response.text)

# Для формирования селекторов используем ChroPath (скрин HW4_3) и тестируем селекторы

# Название курса
#course_names = dom.xpath("//span[@class = 'direction-card__title-text ui-text-body--1 ui-text--medium']/text()")
#print(len(course_names)) # вернул 27

# Срок обучения
#term_trainings = dom.xpath("//div[1]/span[@class = 'ui-text--medium']/text()")
#print(len(term_trainings))

# Cкидка на обучение # вернул 27
#discounts = dom.xpath("//div[@class = 'direction-card__info-label ui-text-heading--5 ui-text--medium gb-landings-product-discount']/text()")
#print(len(discounts)) # вернул 27

# Создаем словарь 

gb_list = []
items = dom.xpath("//div[@class = 'direction-card ui-col-md-6 {[ui_col_xxxl]} ']")
for item in items:
    item_info = {}

    course_name = item.xpath(".//span[@class = 'direction-card__title-text ui-text-body--1 ui-text--medium']/text()")
    term_training = item.xpath(".//div[1]/span[@class = 'ui-text--medium']/text()")
    discount = item.xpath(".//div[@class = 'direction-card__info-label ui-text-heading--5 ui-text--medium gb-landings-product-discount']/text()")

    item_info['course_name'] = course_name
    item_info['term_training'] = term_training
    item_info['discount'] = discount
    gb_list.append(item_info)

print(gb_list)











