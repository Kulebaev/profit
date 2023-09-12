import requests
import json
import os
import sqlite3


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

            delete_data()
            add_data(values)

    except Exception as e:
        return print(e)


def run_daily_job():

    with open('mainSite/config/api_key.json') as api_key_file:
        api_key_data = json.load(api_key_file)

    API_KEY = api_key_data['api_key']  # Замените на путь к файлу с вашим ключом API либо на ключ ключ
    SPREADSHEET_URL = 'https://docs.google.com/spreadsheets/d/1Xl_C6XCs5JA619TLucXFWW-4pPoMOw6hQ2NB3SRUbhk/edit#gid=0'
    RANGE_NAME = 'Лист1' # Наименование листа с которого хотите загружать данные

    get_google_sheets_data(SPREADSHEET_URL, API_KEY, RANGE_NAME)
   

def add_data(rows):

    connection = connections_database()
    cursor = connection.cursor()
    
    # Получение данных из Google Sheets (предполагается, что у вас есть код, который извлекает данные из Google Sheets и сохраняет их в переменную rows)
    for row in rows:
        if len(row) >= 2:  # Проверяем, что есть как минимум 2 столбца данных
            name = row[0]
            price = row[1]

            # SQL-запрос для вставки данных в таблицу
            insert_query = "INSERT INTO mainSite_product (name, price) VALUES (?, ?);"

            # Выполнение запроса с параметрами
            cursor.execute(insert_query, (name, price))

    # Сохранение изменений в базе данных
    connection.commit()

    # Закрытие соединения с базой данных
    connection.close()


def connections_database():
    database_path = 'D:\Программы\profit\profITSite\db.sqlite3'
    connection = sqlite3.connect(database_path)

    return connection    


def delete_data():
    connection = connections_database()
    cursor = connection.cursor()
    # SQL-запрос для удаления всех записей из таблицы
    delete_query = 'DELETE FROM mainSite_product;'

    # Выполнение запроса
    cursor.execute(delete_query)

    # Сохранение изменений в базе данных
    connection.commit()

    # Закрытие соединения с базой данных
    connection.close()

# Планирование выполнения функции каждый день в определенное время
run_daily_job()