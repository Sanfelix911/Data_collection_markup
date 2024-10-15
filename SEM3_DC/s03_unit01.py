import json
from pymongo import MongoClient

# Подключение к серверу MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Выбор базы данных и коллекции
db = client['town_cary']
collection = db['crashes']

# Чтение файла JSON
with open('crash-data.json', 'r') as file:
    data = json.load(file)

data = data['features']


