from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
import json

driver = webdriver.Chrome()
driver.get("https://spb.streetfoot.ru")

time.sleep(1)
search_1 = driver.find_element(By.XPATH, "//div/input[@placeholder = 'Поиск среди 1500 моделей...']")
time.sleep(3)
search_1.send_keys("подростковые")
time.sleep(1)
search_1.submit()
time.sleep(1)
#assert "подростковые" in driver.title
#name_elements = driver.find_elements(By.XPATH,"//a/h3")
#print(name_elements[0].text)
#priсe_elements = driver.find_elements(By.XPATH,"//span[@class = 'woocommerce-Price-amount amount']")
#print(priсe_elements[0].text)
#url_elements = driver.find_elements(By.XPATH,"//ul[@class = 'products']/li/a/@href")
#print(url_elements[0].get_attribute("href"))

shoes = []
    
while True:
    shoes_elements = driver.find_elements(By.XPATH,"//a[@class = 'woocommerce-LoopProduct-link']")

    for shoes_element in shoes_elements :
        name_elements = driver.find_elements(By.XPATH,"//a/h3")
        price_elements = driver.find_elements(By.XPATH,"//span[@class = 'woocommerce-Price-amount amount']")
        shoes.append({"name_elements" : name_elements, "price_elements" : price_elements})

    next = driver.find_elements(By.XPATH,"//li/a[@class ='next page-numbers']")
    if not next:
        break

    next[0].click()
    time.sleep(1)

with open('shoes_result.csv', 'w', encoding='U8', newline='') as file:
    writer = csv.DictWriter(file ,fieldnames= ["name_elements","price_elements"] )
    writer.writeheader()
    writer.writerows(shoes)

with open('shoes_result.json', 'w',  encoding='U8') as file:
    json.dump(shoes)




driver.close()

#for unit in shoes:
#   print(unit[name_elements],unit[price_elements])





