from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Настройки для Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск в фоновом режиме

# Путь к ChromeDriver
#service = Service('/path/to/chromedriver')

# Запуск браузера
driver = webdriver.Chrome(service=service, options=chrome_options)

# Открытие веб-страницы
driver.get('https://www.target.com/')

# Извлечение заголовков
headers = driver.find_elements(By.TAG_NAME, 'h2')
for header in headers:
    print(header.text)

# Извлечение ссылок
links = driver.find_elements(By.TAG_NAME, 'a')
for link in links:
    print(link.get_attribute('href'))

# Закрытие браузера
driver.quit()
