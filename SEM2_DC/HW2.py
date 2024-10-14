import requests
from bs4 import BeautifulSoup
import json


base_url = 'http://books.toscrape.com/'


main_page_response = requests.get(base_url)
print(f'Основной URL статус: {main_page_response.status_code}')
main_page_soup = BeautifulSoup(main_page_response.text, 'html.parser')


category_links = [base_url + x.get('href') for x in main_page_soup.find('ul', class_='nav-list').find_all('a', href=True)[1:]]  


books_info = []


def extract_book_info(article):
    title = article.find('h3').find('a')['title']
    price = article.find('p', class_='price_color').text[2:]  
    stock_text = article.find('p', class_='instock availability').text.strip()
    stock_numbers = [int(s) for s in stock_text.split() if s.isdigit()]
    stock = stock_numbers[0] if stock_numbers else 0  
    
    
    book_url = article.find('h3').find('a')['href']
    book_url = base_url + 'catalogue/' + book_url.replace('../../../', '')
    book_response = requests.get(book_url)
    print(f'Статус страницы книги {title}: {book_response.status_code}')
    book_soup = BeautifulSoup(book_response.text, 'html.parser')
    description_tag = book_soup.find('meta', attrs={'name': 'description'})
    description = description_tag['content'].strip() if description_tag else 'No description'
    
    return {
        'title': title,
        'price': float(price.replace('£', '')),
        'stock': stock,
        'description': description
    }



for category_link in category_links:
    while True:
        response = requests.get(category_link)
        print(f'Статус категории {category_link}: {response.status_code}')
        if response.status_code != 200:
            break
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article', class_='product_pod')
        
        for article in articles:
            book_info = extract_book_info(article)
            books_info.append(book_info)
        
       
        next_button = soup.find('li', class_='next')
        if next_button:
            next_page_url = next_button.find('a')['href']
            category_link = '/'.join(category_link.split('/')[:-2]) + '/' + next_page_url
        else:
            break


with open('books_info.json', 'w', encoding='utf-8') as f:
    json.dump(books_info, f, ensure_ascii=False, indent=4)

