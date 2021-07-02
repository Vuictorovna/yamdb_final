from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .validators import year_validator

User = get_user_model()


class Genre(models.Model):
    name = models.CharField(verbose_name="Жанр", max_length=25)
    slug = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=25)
    slug = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        verbose_name="Наименование",
        db_index=True,
        max_length=50,
        unique=True,
        blank=False,
    )
    year = models.PositiveSmallIntegerField(
        verbose_name="Год выхода.", validators=[year_validator], blank=True
    )
    description = models.TextField(
        verbose_name="Описание", max_length=50, null=True
    )
    genre = models.ManyToManyField(
        Genre, verbose_name="Жанр", related_name="titles", blank=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        related_name="titles",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = [
            "-id",
        ]
        verbose_name = "Назввание"
        verbose_name_plural = "Названия"


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        verbose_name="Название",
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    text = models.TextField(verbose_name="Текст")
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    score = models.IntegerField(
        verbose_name="Оценка",
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    pub_date = models.DateTimeField(
        verbose_name="Дата публикации", auto_now_add=True
    )

    class Meta:
        ordering = [
            "-pub_date",
        ]
        verbose_name = "Обзор"
        verbose_name_plural = "Обзоры"


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        verbose_name="Комметарий",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.TextField(
        verbose_name="Текст комментария",
    )
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    pub_date = models.DateTimeField(
        verbose_name="Дата публикации", auto_now_add=True
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
