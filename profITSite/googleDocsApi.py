import requests
import schedule
import time
import json
import os
import django
# Установите переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "profITSite.settings")
# Настройки Django
django.setup()
# Модели проекта
from mainSite.models import Product

UPDATE_TIME = "12:00"


def get_google_sheets_data(spreadsheet_url, api_key, range_name):

    
    # Извлекаем идентификатор таблицы из URL
    spreadsheet_id = spreadsheet_url.split('/')[-2]

    # URL для доступа к данным таблицы
    base_url = f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range_name}'

    # Параметры запроса, включая API ключ
    params = {
        'key': api_key,
    }

    try:
        # Отправляем GET-запрос к API Google Sheets
        response = requests.get(base_url, params=params)

        # Проверяем статус ответа
        if response.status_code == 200:
            data = response.json()
            values = data.get('values', [])

            Product.objects.all().delete()

            for row in values:
                if len(row) >= 2:  # Проверяем, что есть как минимум 2 столбца данных
                    name = row[0]  # Здесь можно определить соответствие столбцам
                    price = row[1]
                    print(name, price)
                    # Создаем и сохраняем объект модели Product
                    product = Product(name=name, price=price)
                    product.save()

    except Exception as e:
        return print(e)


def run_daily_job():

    with open('mainSite/config/api_key.json') as api_key_file:
        api_key_data = json.load(api_key_file)

    API_KEY = api_key_data['api_key']  # Замените на путь к файлу с вашим ключом API
    SPREADSHEET_URL = 'https://docs.google.com/spreadsheets/d/1Xl_C6XCs5JA619TLucXFWW-4pPoMOw6hQ2NB3SRUbhk/edit#gid=0'
    RANGE_NAME = 'Лист1'

    get_google_sheets_data(SPREADSHEET_URL, API_KEY, RANGE_NAME)
   

# Планирование выполнения функции каждый день в определенное время
schedule.every().day.at(UPDATE_TIME).do(run_daily_job)


while True:
    schedule.run_pending()
    time.sleep(1)  # Пауза в секундах, чтобы избежать высокой загрузки процессора
