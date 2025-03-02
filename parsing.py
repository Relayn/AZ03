import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL страницы с диванами на divan.ru
url = "https://www.divan.ru/category/divany"

# Заголовки для имитации браузера
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

# Отправляем запрос к сайту
response = requests.get(url, headers=headers)

# Проверяем, успешно ли загрузили страницу
if response.status_code == 200:
    # Парсим HTML-код страницы
    soup = BeautifulSoup(response.content, 'html.parser')

    # Находим элементы с ценами (предполагаем, что они в тегах <span> с классом 'price')
    price_elements = soup.find_all('span', {'data-testid': 'price'})

    # Извлекаем и очищаем цены
    prices = []
    for price in price_elements:
        price_text = price.get_text().replace('руб.', '').replace(' ', '').strip()
        try:
            prices.append(float(price_text))
        except ValueError:
            continue  # Пропускаем некорректные значения

    # Если данные получены, сохраняем их в CSV-файл
    if prices:
        # Создаём DataFrame и сохраняем в CSV
        df = pd.DataFrame(prices, columns=['Цена'])
        df.to_csv('divan_prices.csv', index=False)
        print("Цены успешно сохранены в divan_prices.csv")

        # Загружаем данные из CSV-файла
        df = pd.read_csv('divan_prices.csv')

        # Вычисляем среднюю цену
        average_price = df['Цена'].mean()
        print(f"Средняя цена на диваны: {average_price:.2f} руб.")

        # Строим гистограмму
        plt.hist(df['Цена'], bins=20, color='blue', edgecolor='black')
        plt.title('Гистограмма цен на диваны')
        plt.xlabel('Цена (руб.)')
        plt.ylabel('Частота')
        plt.grid(True)
        plt.show()
    else:
        print("Не удалось извлечь цены с сайта.")
else:
    print(f"Не удалось загрузить страницу. Код ответа: {response.status_code}")