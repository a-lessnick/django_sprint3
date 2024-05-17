""" Настройка административного раздела сайта."""
from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Category
from .models import Location
from .models import Post


# Удаление регистрации неиспользуемой модели 'Group'
admin.site.unregister(Group)


# Регистрация моделей приложения.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Отображение категорий в панели администратора."""

    list_display = ('title', 'slug', 'is_published')
    search_fields = ['title', 'description', 'slug']
    list_filter = ['is_published']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """ Отображение мест в панели администратора."""

    list_display = ('name', 'is_published')
    search_fields = ['name']
    list_filter = ['is_published']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Отображение публикаций в панели администратора."""

    list_display = ('title', 'author', 'pub_date')
    search_fields = ['title', 'text']
    list_filter = ['author',
                   ('pub_date', admin.DateFieldListFilter)
                   ]
