# client_table
### Установка и настройка
1. Для изоляции зависимостей проекта рекомендуется использовать виртуальное окружение.
```bash
python -m venv venv
```
   Запуск виртуального окружения:

Windows:
```bash
.\djvenv\Scripts\activate
```
Linux\macOS:
```bash
source djvenv/bin/activate
```
2. Клонируйте проект:
```bash
git clone
```
3 Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Для безопасного необходимо SECRET_KEY добавить в `.env` файл, который создаётся в Django проекте.
```
SECRET_KEY=ваш_секретный_ключ_django
```
5. Настройте базу данных и выполните миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```
  Эта команда создаст необходимые таблицы в базе данных согласно моделям приложений Django.
  
6. Синтезировать данные для БД:

Пример ввода данных:

Таблица пользователей:
  ```bash
  python manage.py shell
  from data.models import User
  User.objects.create_user('ivan', 'Иванов И.И.', 'ivan')
  User.objects.create_user('danila', 'Данилов.С.Ю', '123') 
  ```
  
Таблица клиентов:

  Для примера можно сгенирировать данные, используя библиотеку Faker
   ```bash
  python manage.py fake_users
  ```
7. Запустите сервер разработки:
```bash
python manage.py runserver
```
