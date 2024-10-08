import requests
import json
from pprint import pprint

client_id = "BVIIJEWHRKR21QP3LGBJRXDFMSDOEKFEATEOUKO11AJCD2UY"
client_secret = "KYGRPCBCPVQEMZF4WUVRT0S1FCI4P3GF0KW500GY11R1RZ0VT"

url = f"https://api.foursquare.com/v2/venues/search?categoryId=4d4b7105d754a06374d81259&limit=5&client_id={client_id}&client_secret={client_secret}"

response = requests.get(url)
data = response.json()


for venue in data["response"]["venues"]:
    name = venue["name"]
    address = venue["location"]["address"]
    rating = venue["rating"]

    print(f"{name} - {address}, рейтинг: {rating}")