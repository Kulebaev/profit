from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import sqlite3

@csrf_exempt
def process_json(request):
    if request.method != 'POST':
        return HttpResponse('Метод не поддерживается', status=405)
    try:
        # Получаем JSON данные из POST запроса
        json_data = json.loads(request.body)

        # delete_data()
        
        return add_data(json_data)

    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Ошибка в JSON формате: ' + str(e)}, status=400)
        

@csrf_exempt
def process_json_full_clear(request):
    if request.method != 'POST':
        return HttpResponse('Метод не поддерживается', status=405)
    return delete_data()
        

def connections_database():
        
        database_path = 'D:\Программы\profit\profITSite\db.sqlite3'
        connection = sqlite3.connect(database_path)
    
        return connection    
    
def add_data(json_data):
    connection = connections_database()
    cursor = connection.cursor()

    # Создаем и сохраняем объект Product для каждой пары
    for item in json_data:
        name = item['name']
        price = item['price']
        ref_key = item['ref_key']

        # Проверяем, существует ли запись с данным ref_key
        cursor.execute("SELECT * FROM mainSite_product WHERE ref_key = ?", (ref_key,))
        existing_product = cursor.fetchone()

        if existing_product:
            # Если запись существует, обновляем данные
            update_query = "UPDATE mainSite_product SET name = ?, price = ? WHERE ref_key = ?;"
            cursor.execute(update_query, (name, price, ref_key))
        else:
            # Если запись не существует, вставляем новую запись
            insert_query = "INSERT INTO mainSite_product (name, price, ref_key) VALUES (?, ?, ?);"
            cursor.execute(insert_query, (name, price, ref_key))

    # Сохранение изменений в базе данных
    connection.commit()
    
    # Закрытие соединения с базой данных
    connection.close()
    return JsonResponse({'message': 'JSON данные успешно обработаны и записаны в базу данных'})     
    
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

    return JsonResponse({'success': 'Удалилось'})