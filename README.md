
**Сеть по продаже электроники**

**Описание задачи:**

Создание веб-приложения с API-интерфейсом и админ-панелью.

Реализована модель сети по продаже электроники.

Сеть представляет собой иерархическую структуру из трех уровней:

o	завод;

o	розничная сеть;

o	индивидуальный предприниматель.

Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, т. е. завод всегда находится на уровне 0, а если розничная сеть относится напрямую к заводу, минуя остальные звенья, ее уровень — 1.


**Запуск проекта(локально).**

1.Клонируйте проект

    git clone git@github.com:DuckRainbow/retailing.git
    
2.Создайте виртуальное окружение

     python3 - m venv .venv
     
3.Активируйте виртуальное окружение venv

     venv/Scripts/activate
     
4.Установите зависимости виртуального окружения

     pip install -r requirements.txt
     
5.Переименуйте файл .env.sample в .env и заполните необходимые данные для запуска локально.

6.Создайте базу данных в PostgreSQL , которую указали в файле .env в параметре POSTGRES_DB

7.При локальном запуске проекта выполните миграции

      python3 manage.py migrate
      
8.Создайте суперпользователя

      python3 manage.py csu
      
9.Запустите проект

      python3 manage.py runserver
      
10.Перейдите в админку по адресу http://127.0.0.1:8000/admin. Введите параметры учетной записи admin@example.com и пароль 123qwe.

11.Для начала работы ознакомиться с документацией по адресу http://127.0.0.1:8000/swagger/ или http://127.0.0.1:8000/redoc/

