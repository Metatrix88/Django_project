# Как запустить данный проект:
1. Создать папку у себя локально где будет лежать проект.
2. Зайти в эту папку с помощью редактора кода (я использую Visual Studio Code)
3. Создать в этой папке виртуальное окружение.

    Создаем виртуальное окружение:
    * python3 -m venv env

    Активируем виртуальное окружение:
    * source env/bin/activate

(Для деактивации в конце пишем /deactivate)

Пример:
```
(env) andrey@devid:~/Python/Django_project (main)$
```
5. Клонировать проект с GitHub репозитория
```
git clone git@github.com:Metatrix88/Django_project.git
```
6. Создаем рядом с папкой проекта две папки под названием static и media, в проекте /home/andrey/Python/Django_project/src/proj находим файл settings.py и иправляем пути в папкам static и media

```
STATIC_URL = '/static/'
STATIC_ROOT = '/home/andrey/Python/static'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/andrey/Python/media'
```
7.  Перейти непосредсвенно в сам проект папка src и установить зависимости:
```
pip install -r requirements.txt
 ```
8. Создаем файл local_vars.py рядом с settings.py файлом, добавляем local_vars в файл gitignore, в файле settings не забваем импортировать данный файл.
```
from . import local_vars
```
В файле local_vars создаем следующие строчки
```
DJANGO_KEY = 'django-insecure-wug083v&b+ezb)!w+x7xok)eiy+iqukgy0vlxv7s(&-ln@2afa'
DJANGO_DEBUG = True
```
9. Далее делаем следующие команды:
```
python3 manage.py collectstatic
python3 manage.py makemigrations
python3 manage.py migrate
```
10.  Создаем администратора:
```
python3 manage.py createsuperuser
```
Вводим login, email, password

11.  Запускаем наш локальный сервер:
```
python3 manage.py runserver
```
Переходим по ссылке которая будем в выводе либо вводи в браузере http://127.0.0.1:8000/admin/
