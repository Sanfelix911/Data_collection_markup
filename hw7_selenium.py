from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv


driver = webdriver.Chrome()
driver.get("https://spb.streetfoot.ru")

time.sleep(1)

#Заходим в поле поиска , вводим "подростковые"

search_1 = driver.find_element(By.XPATH, "//div/input[@placeholder = 'Поиск среди 1500 моделей...']")
time.sleep(3)
search_1.send_keys("подростковые")
time.sleep(1)
search_1.submit()
time.sleep(1)

#Тетстируем селлекторы

# name_elements = driver.find_elements(By.XPATH,"//a/h3/")
# print(name_elements[0].text)
# priсe_elements = driver.find_elements(By.XPATH,"//span[@class = 'woocommerce-Price-amount amount']")
# print(priсe_elements[0].text)

# Цикл заполнения словаря
 
shoes = []
    
while True:
    shoes_elements = driver.find_elements(By.XPATH,"//div[@class = 'img']")

    for element in shoes_elements:
        name_elements = driver.find_element(By.XPATH,".//a/h3").text
        price_elements = driver.find_element(By.XPATH,".//span[@class = 'woocommerce-Price-amount amount']").text
        shoes.append({"name_elements" : name_elements, "price_elements" : price_elements})

    next = driver.find_elements(By.XPATH,"//li/a[@class ='next page-numbers']")
    if not next:
        break

    next[0].click()
    time.sleep(1)

driver.close()

with open('shoes_result.csv','w', encoding='U8',  newline='') as file:
    writer = csv.DictWriter(file ,fieldnames= ["name_elements","price_elements"] )
    writer.writeheader()
    writer.writerows(shoes)







