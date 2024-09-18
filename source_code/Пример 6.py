from bs4 import BeautifulSoup
import requests
import os

url = 'https://www.washingtonpost.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Создание директории для изображений
os.makedirs('images', exist_ok=True)

# Извлечение и сохранение изображений
for img in soup.find_all('img', src=True):
    img_url = img['src']
    img_response = requests.get(img_url)
    img_name = os.path.basename(img_url)
    with open(os.path.join('images', img_name), 'wb') as file:
        file.write(img_response.content)



