from bs4 import BeautifulSoup
import requests

base_url = 'https://books.toscrape.com/'
response = requests.get(base_url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')


# Извлечение всех заголовков h1
headers = soup.find_all('h1')
for header in headers:
    print(header.text)

# Извлечение всех ссылок
links = soup.find_all('a', attrs={'href': True})
for link in links:
    print(link['href'])


# Извлечение элементов с классом 'example-class'
elements = soup.find_all(class_='example-class')
for element in elements:
    print(element.text)


with open('headlines.txt', 'w') as file:
    for header in headers:
        file.write(header.text + '\n')


import csv

data = [['Title', 'URL']]
for link in links:
    data.append([link.text, link['href']])

with open('links.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)


import json

data = [{'title': link.text, 'url': link['href']} for link in links]

with open('links.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


