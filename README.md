### Workflow status
![YamDB workflow](https://github.com/Vuictorovna/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Описание/ Description
Проект **YaMDb** собирает отзывы пользователей на произведения в категориях: «Книги», «Фильмы» и «Музыка».
В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха. Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). _Новые жанры может создавать только администратор_.
Благодарные или возмущённые читатели оставляют к произведениям текстовые отзывы и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти). Из множества оценок автоматически высчитывается средняя оценка произведения.
**Note:** Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
***
**The YaMDb** project collects user reviews of works in three categories: "Books", "Movies" and "Music".
For example, in the category “Books” there may be works “Winnie-the-Pooh” and “The Martian Chronicles”, and in the category “Music” - Orchestral suites by Bach. A piece can be assigned a genre from a list of preset ones (for instance , "Fairy tale", "Rock" or "Art film"). New genres can only be created by the administrator.
Grateful or outraged readers leave text reviews and rate works (in the range from one to ten). The average score is automatically calculated from the set of ratings.
**Note:** The works themselves are not stored in YaMDb, you cannot watch a movie or listen to music here.

### Технологии/ Technology:
* Python 3.8.5
* Django 3.0.5
* Gunicorn 20.1.0
* Nginx 1.19.3
* Postgres 12.4

### Команды для работы с приложением/ How to start:
-  Клонировать приложение к себе в репозиторий/ Clone the app to your repository
```bash
git clone https://github.com/Vuictorovna/yamdb_final.git
```
- Необходимые переменные окружения, сохраненные в .env/ Required environment variables saved in .env
    - DB_ENGINE
    - DB_NAME
    - POSTGRES_USER
    - POSTGRES_PASSWORD
    - DB_HOST
    - DB_PORT

- Запуск приложения/ App launch
```bash
docker-compose up
```
- Сделать миграции/ Make migrations
```bash
docker-compose exec web python manage.py makemigrations api

docker-compose exec web python manage.py migrate --noinput
```
- Создание суперпользователя/ Create superuser
```bash
docker-compose exec web python manage.py createsuperuser
```
- Подготовка статики проекта/ Preparing project statics
```bash
docker-compose exec web python manage.py collectstatic --no-input
```
- Запуск тестов/ Running tests
```bash
docker-compose exec web python manage.py pytest
```
### Авторы
Оля Сахаревич, студентка факультета Бэкэнд Яндекс.Практикум/ Volha Sakharevich, Yandex.Practicum student
