# Library online
# Описание

Сайт Library online позволяет хранить описание различных книг.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:


```
cd library
```

Запустить проект в контейнерах:

```
sudo docker compose up --d
```

Запустить миграции:

```
sudo docker compose exec project-library-1 python manage.py migrate
sudo docker compose exec project-library-1 python manage.py makemigrations
```


Создать суперпользователя для работы в аминке:

```
Админка досупна по url http://127.0.0.1/admin/
sudo docker exec -it project-library-1 bash
python manage.py createsuperuser
```

Доступны следующие эндпойнты API:

```
http://127.0.0.1/api/books/ - для работы с книгами (GET, POST, PUTCH, DELETE)
http://127.0.0.1/api/users/ - для работы с пользователями (GET, POST)
```


Примеры запросов:

```
http://127.0.0.1/api/books/
POST запрос для создания книги в формате JSON
{
    "title": "Властелин колец",
    "author": "Д.Р.Р. Толкиен",
    "pub_date": "2023-11-22",
    "isbn": 123456789
}
```
```
http://127.0.0.1/api/users/
POST запрос для регистрации нового пользователя в формате JSON
{
    "email": "admin@admin.ru",
    "username": "admin"
}
```

Использованое програмное обеспечение:

```
Python 3.9.10
Django 3.2
djangorestframework 3.14.0
postgres 13.10
celery 4.4.7
redis 3.5.3
flower 0.9.7

```

Автор:

```
kanaev-ch@yandex.ru
kanaev.ch@gmail.com
```
