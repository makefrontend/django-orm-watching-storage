# Проект "Пульт охраны банка"
Интерфейс для пульта охраны банка, в котором доступна информация о посетителях, времени пребывания с классификацией по подозрительными визитам. 

## Как установить
* У вас должен быть установлен `python 3.8.*`
* `git clone https://github.com/makefrontend/django-orm-watching-storage.git`
* `pip install -r requirements.txt`

## Как настроить
Для переменных окружения создайте файл `.env`, разместите его в папку `project` и произведите следующие настройки:
* `DB_ENGINE=var`
* `DB_HOST=var`
* `DB_PORT=var`
* `DB_NAME=var`
* `DB_USER=var`
* `DB_PASSWORD=var`
* `SECRET_KEY=var`
* `DEBUG=var`
* `ROOT_URLCONF=var`
* `ALLOWED_HOSTS=var`

## Как запустить
В терминале перейдите в папку проекта и выполните команду `python manage.py runserver 127.0.0.1:8000`. После этого сайт будет доступен по адресу `127.0.0.1:8000`
