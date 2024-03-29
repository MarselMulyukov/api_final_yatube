# API for Yatube-The Last Social Media You'll Ever Need
Социальная сеть, где можно публиковать личные дневники.
Пользователи смогут просматривать дневники других авторов, подписываться на авторов и комментировать их записи.
Записи можно отправить в сообщество и посмотреть там записи разных авторов.
Для доступа к API необходимо в запросе к серверу передавать токен. Токен можно получить по логину и паролю.

Пример запроса к API - создание поста:
отправляем POST запрос к странице ```127.0.0.1:8000/api/v1/posts/```
с содержимым
- ```headers = {'Authorization': 'Bearer <ваш токен>'}```
- ```payload = {'text': 'Привет я текст'}```

получим в теле ответа:
- ```{"id": 5, "text": "Привет я текст", "author": "MARSIK", "pub_date": "2022-12-07T09:42:28.943393Z"}```

Для запуска на локальной машине необходимо:
1. Склонировать репозиторий себе на локальную машину: 
```git clone https://github.com/MarselMulyukov/api_final_yatube.git```
2. В директории api_final_yatube создать виртуальное окружение:
```python -m venv venv```
3. Запустить виртуальное окружение:
```source venv/scripts/activate```
4. Установить зависимости из файла requirements.txt:
```pip install -r requirements.txt```
5. Создать базу данных: 
```python manage.py migrate```
6. Запустить сервер на локальной машине:
```python manage.py runserver```
7. Открыть в браузере страницу http://127.0.0.1:8000/

Технологии: Django Rest Framework, SQLite
