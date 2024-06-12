import requests
from bs4 import BeautifulSoup
import time
import csv

page = 1

with open('biblusi_books.csv', mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Page', 'Title'])


    while page < 6:
        base_url = f"https://biblusi.ge/products?category=291&category_id=300&page={page}"
        response = requests.get(base_url)
        html = response.text

        if response.status_code == 200:
            soup = BeautifulSoup(html, 'html.parser')
            book_section = soup.find('div', class_='row')

            all_books = book_section.find_all('acronym')
            titles = [acronym['title'] for acronym in all_books if 'title' in acronym.attrs]
            for title in titles:
                writer.writerow([page, title])

        time.sleep(15)
        page += 1
