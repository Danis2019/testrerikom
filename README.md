#Docker
Не запускайте, туда не прикручена кафка
# Версии ПО
##### Java 7
##### kafka 2.12-3.2.0
##### MySql 8.0.28
##### Django 4.0.4
# Как запускать
1. Запуск kafka
* bin/zookeeper-server-start.sh config/zookeeper.properties
* bin/kafka-server-start.sh config/server.properties
2. Запуск Django 
* python manage.py runserver
* Укажите вашу базу данных в testrerikom/settings.py
`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'NameDB',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'Your password',
        'PORT': '3306',
    }
}`
3. Запуск listiner.py
4. Выполняете Post запрос на роуте ../api/v1/message
`
{
    "user_id" = 123
    "message" = "text"
} 
`