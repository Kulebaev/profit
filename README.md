README для приложения на Django с интеграцией 1С, базой данных на хосте CVS и Google Docs API
Описание
Этот проект представляет собой одностраничный лэндинг с интеграцией с системой 1С через REST API. Приложение также содержит базу данных, в которой хранится информация о товарах, включая название и цену. Кроме того, приложение имеет интеграцию с Google Docs API для загрузки и обновления прайс-листов из документов Google Docs.
Телеграмм бот для отправки значений формы в чат телегармм.

Требования
Перед началом использования этого приложения, убедитесь, что у вас есть следующее:

Python 3.x установлен на вашем сервере.
Установлен фреймворк Django. Вы можете установить его с помощью следующей команды:

pip install Django
Доступ к серверу 1С через REST API.
Доступ к CVS для хранения базы данных.
Доступ к Google Docs API и настроенные учетные данные для работы с документами Google Docs.

Установка и запуск
Склонируйте репозиторий на вашем сервере:

git clone <URL репозитория>
Перейдите в каталог проекта:

cd <название проекта>
Создайте виртуальное окружение (рекомендуется для изоляции зависимостей):

python -m venv venv
Активируйте виртуальное окружение:

source venv/bin/activate  # На Linux/macOS
или

venv\Scripts\activate  # На Windows
Установите зависимости:

pip install -r requirements.txt

римените миграции для создания таблиц базы данных:

python manage.py migrate
Запустите сервер разработки:

python manage.py runserver
Приложение будет доступно по адресу http://localhost:8000/ в вашем браузере.

Использование
Приложение теперь готово к использованию.

Автор
https://github.com/Kulebaev

Адрес сайта