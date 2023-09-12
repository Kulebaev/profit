from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import datetime
import pytz


@csrf_exempt
def process_json(request):
    if request.method != 'POST':
        return HttpResponse('Метод не поддерживается', status=405)

    try:
    # Получаем JSON данные из POST запроса
        json_data = json.loads(request.body)

        # Путь к директории, где должен быть создан файл
        directory_path = '/home/src/profit/profITSite/mainSite/json'
        
        # Определяем часовой пояс Москвы
        moscow_timezone = pytz.timezone('Europe/Moscow')
        
        # Получаем текущую дату и время
        current_time_utc = datetime.datetime.now(pytz.utc)
        
        # Преобразуем текущее время в часовой пояс Москвы
        current_time_msk = current_time_utc.astimezone(moscow_timezone)
        
        # Генерируем уникальное имя файла на основе даты и времени
        date_to_write = current_time_msk.strftime('%Y-%m-%d_%H_%M_%S')
        
        file_name = f'output_{date_to_write}.json'

        # Полный путь к файлу
        file_path = os.path.join(directory_path, file_name)

        # Создаем JSON данные для записи
        data_to_write = json_data

        # Добавляем дату и время получения
        data_to_write["timestamp"] = current_time_msk.strftime('%Y-%m-%d %H:%M:%S')

        # Проверяем, существует ли директория, и если нет, то создаем её
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        # Записываем JSON данные в файл
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data_to_write, file, ensure_ascii=False, indent=4)

        # Проверяем, записался ли файл успешно
        if os.path.exists(file_path):
            return JsonResponse({'message': 'JSON данные успешно обработаны и записаны в файл ' + file_name})
        else:
            return JsonResponse({'error': 'Ошибка записи в файл ' + file_name}, status=500)

    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Ошибка в JSON формате: ' + str(e)}, status=400)