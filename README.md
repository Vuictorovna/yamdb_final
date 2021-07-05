### workflow status
![YamDB workflow](https://github.com/Vuictorovna/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# YaMDb_final
### Описание
Проект YaMDb собирает отзывы пользователей на произведения в категориях: «Книги», «Фильмы» и «Музыка».
***
В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха. Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). _Новые жанры может создавать только администратор_.
***
Благодарные или возмущённые читатели оставляют к произведениям текстовые отзывы и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти). Из множества оценок автоматически высчитывается средняя оценка произведения.
***
**Note:** Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

### Посмотреть на то, как работает проект можно по этому адресу http://84.252.143.117/redoc

### Технологии
* Python 3.8.5
* Django 3.0.5
* Gunicorn 20.1.0
* Nginx 1.19.3
* Postgres 12.4

### Команды для работы с приложением
-  Клонировать приложение к себе в репозиторий
```bash
git clone https://github.com/Vuictorovna/yamdb_final.git
```
- Необходимые переменные окружения, сохраненные в .env
    - DB_ENGINE
    - DB_NAME
    - POSTGRES_USER
    - POSTGRES_PASSWORD
    - DB_HOST
    - DB_PORT

- Запуск приложения
```bash
docker-compose up
```
- Сделать миграции
```bash
docker-compose exec web python manage.py makemigrations api

docker-compose exec web python manage.py migrate --noinput
```
- Создание суперпользователя
```bash
docker-compose exec web python manage.py createsuperuser
```
- Подготовка статики проекта
```bash
docker-compose exec web python manage.py collectstatic --no-input
```
- Запуск тестов
```bash
docker-compose exec web python manage.py pytest
```
### Авторы
Оля Сахаревич, студентка факультета Бэкэнд Яндекс.Практикум
