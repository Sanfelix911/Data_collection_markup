
from pymongo import MongoClient
import json

client = MongoClient("localhost:27017")
db = client.HW3_Erohin
book_info = db.books_info


books_data = book_info.find()

count = book_info.count_documents({})
print(count)


