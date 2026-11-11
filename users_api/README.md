# Users API

Учебный REST API на FastAPI: CRUD для пользователей.

## Запуск
py -m pip install -r requirements.txt
py -m uvicorn main:app --reload

Документация: http://127.0.0.1:8000/docs

## Эндпоинты
- GET /users - список пользователей
- GET /users/{id} - один пользователь
- POST /users - создать
- PUT /users/{id} - изменить
- DELETE /users/{id} - удалить