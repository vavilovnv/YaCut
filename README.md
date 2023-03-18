# YaCut ✂️

Еще один сервис сокращения длинных url-адресов, который позволяет:
* Генерировать уникальные короткие ссылки для переданных url 
* Переадресовывать на исходный url-адрес по короткой ссылке
* Взаимодействовать с эндпоинтами REST API:
	- `/api/id/` — post-запрос на создание короткой ссылки; 
	- `/api/id/<short_id>/` — get-запрос на получение исходного url-адреса по переданной короткой ссылке. 
	
Примеры API запросов приведены в схеме `openapi.yml` в формате документации [Swagger](https://editor.swagger.io/).

## Стек

[![Python][Python-badge]][Python-url]
[![Flask][Flask-badge]][Flask-url]
[![SQLAlchemy][SQLAlchemy-badge]][SQLAlchemy-url]
[![SQLite][SQLite-badge]][SQLite-url]

## Установка и запуск проекта

* Клонировать репозиторий:

```
git clone git@github.com:vavilovnv/yacut.git
```

* Установить и активировать виртуальное окружение:
```
python3 -m venv venv
source venv/bin/activate
```

* Установить зависимости:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

* Выполнить миграции: 
``` 
flask db upgrade 
```

* Запустить приложение: 
``` 
flask run
```

![Watchers Badge](https://img.shields.io/github/watchers/vavilovnv/YaCut.svg])

<!-- MARKDOWN BADGES & URLs -->
[Python-badge]: https://img.shields.io/badge/python%203.9+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54

[Python-url]: https://www.python.org/

[Flask-badge]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white

[Flask-url]: https://flask.palletsprojects.com

[SQLAlchemy-badge]: https://img.shields.io/badge/sqlalchemy-fbfbfb?style=for-the-badge

[SQLAlchemy-url]: https://www.sqlalchemy.org/

[SQLite-badge]: https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white

[SQLite-url]: https://sqlite.org/index.html

