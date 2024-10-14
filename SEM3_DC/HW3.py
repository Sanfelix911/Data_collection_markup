
from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client['hw3_erohin']
book_info = db['book_info']

with open('books_info.json', 'r') as file:
    books_json = json.load(file)

for book in books_json:
    book_info.insert_one(book)

books_data = book_info.find()