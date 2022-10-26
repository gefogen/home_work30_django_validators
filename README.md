*home_work29_django*

### Миграции

- Создать миграции:

python manage.py makemigrations

- Накатить миграцию:

 python manage.py migrate

------------------



### Загрузка данных в БД :

- python manage.py loaddata location.json
- python manage.py loaddata user.json
- python manage.py loaddata category.json
- python manage.py loaddata ad.json

### Для доступа к админке

------------------

Создать администратора набрать команду:

- python manage.py createsuperuser

- Имя: skypro-user
- пароль: user123

Запустить серевер:

### python manage.py runserver
