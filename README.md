# test_uptrader

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Bogdan-Malina/test_uptrader.git
```

```
cd test_uptrader
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

Обновить pip в виртуальном окружении
```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Собрать статические файлы в STATIC_ROOT:
```
python manage.py collectstatic
```

Выполнить миграции:

```
python manage.py makemigrations
```
```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Технологии:
- Python 3.11.2
- Django 4.1.7


