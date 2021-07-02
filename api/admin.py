from django.contrib import admin

from api.models import Category, Genre, Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "year",
        "category",
        "description",
    )
    empty_value_display = "-empty-"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
    )
    empty_value_display = "-empty-"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
    )
    empty_value_display = "-empty-"
