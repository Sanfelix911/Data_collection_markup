import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pprint import pprint

# ua = UserAgent()



# url = "https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab"

url = "https://www.boxofficemojo.com"
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
params = {"ref_": "bo_nb_hm_tab"}

session = requests.session()

response = session.get(url+"/intl", params=params, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# test_link = soup.find("a", {'class': 'a-link-normal'})
rows = soup.find_all('tr')

films = []

for row in rows[2:-1]:
    film = {}

    # area_info = row.find('td', {'class': 'mojo-field-type-area_id'}).find('a')
    area_info = row.find('td', {'class': 'mojo-field-type-area_id'})
    film['area'] = [area_info.getText(), url + area_info.get('href')]

    weekend_info = row.find('td', {'class': 'mojo-field-type-date_interval'})
    film['weekend'] = [weekend_info.getText(), url + weekend_info.get('href')]

    film['realeses'] = int(row.find('td', {'class':'mojo-field-type-positive_integer'}).getText())

    frelease_info = row.find('td', {'class': 'mojo-field-type-release'})
    film['frelease'] = [frelease_info.getText(), url + frelease_info.get('href')]

    try:
        distributor_info = row.find('td', {'class': 'mojo-field-type-studio'})
        film['distributor'] = [distributor_info.getText(), url + distributor_info.get('href')]
    except:
        print('Exception with frelease, object = ', film['frelease'])
        film['distributor'] = None

    film['gross'] = int(row.find('td', {'class': 'mojo-field-type-positive_integer'}).getText())


    films.append(film)


pprint(films)







