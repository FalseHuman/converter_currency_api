# Converter Currence REST API

Конвертер на базе https://cash.rbc.ru/cash/currency.html

### Инструменты

- Python >= 3.9
- Django Rest Framework
- Docker
- Postgres
- NGINX


## Старт

#### 1) В корне проекта создать .env.dev и прописать свои настройки

    DEBUG=1
    SECRET_KEY=SECRET_KEY
    DJANGO_ALLOWED_HOST=localhost
    
    # Data Base
    POSTGRES_DB=имя_твоей_бд
    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_USER=имя_твоего_пользователя
    POSTGRES_PASSWORD=пароль_бд
    POSTGRES_HOST=db
    POSTGRES_PORT=5432

#### 2) Создать образ и запустить контейнер

    docker-compose up --build

##### 3) Создать супер юзера

    docker exec -it converter_api_web
    python manage.py collectstatic
    python manage.py createsuperuser
    python manage.py parser_currency -> парсит список валют с https://cash.rbc.ru
    
##### 4) Перейти по адресу

    http://localhost:8000/api/v1/schema/swagger-ui/
    # or
    http://localhost:8000/api/v1/schema/redoc/

                                                        
##### 0) Если нужно очистить БД

    docker-compose down -v
