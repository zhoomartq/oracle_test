## Тестовое задание от компании Oracle Digital

### _Документация API_ (автодокументирование на swagger (drf-yasg) доступно по адресу http://0.0.0.0:8000/docs/ )

## Школа

С помощью фреймворка Django напишите сайт для автоматизации школьных процессов. На сайте должны быть реализованы следующие функции:
- Регистрация учителя через сайт
- Аутентификация учителя (авторизация через логин и пароль)
- Добавлять, читать, изменять, удалять(CRUD) учеников
- После создания ученика, отправить ему email уведомление
- Поиск учеников
- Отправлять сообщение на mail учеников(рассылка).

## Модели:

    “Ученик”:
        - ФИО
        - Mail
        - Дата рождения
        - Класс
        - Адрес
        - Пол
        - Фото(необязательно)
	“Учитель”:
        - номер телефона
        - Класс
        - Название предмета
	“Класс”:
        - Название
        - Учитель(один)
        - Ученики(много)
	“Школа”:
        - Название
        - Классы

## Примечание
- Модель “Учитель” должен наследоваться от встроенного в django класса “AbstractUser” и заходить на сайт через “номер телефона”. 

## Требования
- Код в репозитории на GitHub
- Понятная документация по установке проекат в файле README.md
- Список всех зависимостей должен храниться в requirements.txt, соответственно можно установить их командой pip install -r requirements.txt
- Разработка должны вестись в virtualenv, но сама директория с virtualenv должна быть добавлена в .gitignore
- По frontend требований никаких не предъявляется. Интерфейс на ваше усмотрение и он не будет оцениваться
- После создания ученика отправлять уведомление использовав django signals
- Запуск через Docker


## Склонируйте репозиторий с помощью git
    https://github.com/zhoomartq/oracle_test.git /HTTPS
    git@github.com:zhoomartq/oracle_test.git /SSH


### В файле ``` runtime.txt ``` указана версия питона

### перед запуском проекта создайте ```.env``` file и настройте бд и вашу почту как в файле ```env.example```


### Чтобы запустить проект на докере введите команду ```docker-compose up -d --build```

# Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

* Создание суперпользователя
```bash
docker-compose exec web python manage.py createsuperuser
```
### Далее введите свои данные для администратора
```bash
Email address: username@username.com
Password: ********
Password (again): ********
Superuser created successfully.
```

## Введите команду ```docker-compose logs -f web``` для отслеживания запросов в приложении

* Приложение будет доступно по адресу: http://0.0.0.0:8000/
* Администрирование приложения будет доступно по адресу: http://0.0.0.0:8000/admin/
* Документация API (автодокументирование на swagger (drf-yasg) доступно по адресу http://0.0.0.0:8000/docs/ )


## Чтобы создать учителя
* Request method: POST
* URL: http://0.0.0.0:8000/teacher/register/
* Body
    * email: 
    * phone_number:
    * password: 
    * class_name:
* Example
```
curl --location --request POST 'http://0.0.0.0:8000/teacher/register/' \
--form 'email=%email' \
--form 'phone_number=%phone_number'
--form 'password=%password'
--form 'class_name=%class_name'
```

## Чтобы получить токен пользователя: 
* Request method: POST
* URL: http://0.0.0.0:8000/teacher/login/
* Body
    * email: 
    * phone_number:
    * password: 
    * class_name:
* Example
```
curl --location --request POST 'http://0.0.0.0:8000/teacher/login/' \
--form 'email=%email' \
--form 'phone_number=%phone_number'
--form 'password=%password'
--form 'class_name=%class_name'
```

## Создаём школу в админ панеле http://0.0.0.0:8000/admin/, далее в той же админ панеле создаётся Класс (пишем название класса (прим 11 В), выбираем учителя и школу)

## Создание ученика можно также создать в админ панеле http://0.0.0.0:8000/admin/ или  в свагере http://0.0.0.0:8000/docs/)

* Request method: POST
* URL: http://0.0.0.0:8000/api/students/
* Body: 
    * classes: id класса:
    * full_name:
    * mail: example@example.com
    * date_of_birth: YYYY-MM-DD 
    * address:
    * gender: [ M, F, O ]
    * photo:

## Для получения списка учеников http://0.0.0.0:8000/api/students/
* Request method: GET
* URL: http://0.0.0.0:8000/api/students/

## Для получения изменения ученика http://0.0.0.0:8000/api/students/
* Request method: PUT
* URL: http://0.0.0.0:8000/api/students/
* ID: id ученика

## Для получения удаления ученика http://0.0.0.0:8000/api/students/
* Request method: DELETE
* URL: http://0.0.0.0:8000/api/students/
* ID: id ученика

## Для поиска учеников http://0.0.0.0:8000/api/students/?search=['full_name', 'mail', 'address', 'gender']
* Request method: GET
* URL: http://0.0.0.0:8000/api/students/

## Для отправки рассылки  http://0.0.0.0:8000/multiple-mail/
* Request method: POST
* URL: http://0.0.0.0:8000/multiple-mail/
* Body: 
    * title: 
    * text:


# Детальнее можно ознакомиться в ```swagger``` документации http://0.0.0.0:8000/docs/ 
