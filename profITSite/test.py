import sqlite3

# Подключение к базе данных SQLite
database_path = '/home/src/profit/profITSite/db.sqlite3'
connection = sqlite3.connect(database_path)
cursor = connection.cursor()

# SQL-запрос для выборки всех записей из таблицы
select_query = 'SELECT * FROM mainSite_product;'

# Выполнение запроса
cursor.execute(select_query)

# Получение результатов запроса
results = cursor.fetchall()

# Закрытие соединения с базой данных
connection.close()

# Вывод результатов на экран
for row in results:
    print(row)
