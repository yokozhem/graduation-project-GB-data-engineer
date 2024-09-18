from bs4 import BeautifulSoup
import requests

url = 'https://www.washingtonpost.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Извлечение заголовков статей
titles = [header.text for header in soup.find_all('h2')]
# Извлечение ссылок на статьи
links = [a['href'] for a in soup.find_all('a', href=True)]

# Сохранение данных в CSV
import csv
with open('news_articles.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link'])
    writer.writerows(zip(titles, links))


