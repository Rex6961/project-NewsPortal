# project-NewsPortal

Это проект новостного портала.
В нем встроены авторизация, аутентификация и идентификация регистрации пользователя.
Есть еженедельная рассылка и рассылка новых новостей пользователям которые подписаны на данные категории статей.

Для запуска проекта необходимо установить:
  1. Django==4.1.5
  2. Celery==5.2.7
  3. django-allauth==0.52.0
  4. django-schelduler==0.6.2
  5. django-filter==22.1
  6. eventlet==0.33.2
  7. redis==4.4.2

В терменалах произвести запуск с помощью комманд:
  1. python manage.py runserver
  2. celery -A NewsPaper worker -l info -P eventlet
  3. celery -A NewsPaper beat -l info

Проект в стадии разработки.
