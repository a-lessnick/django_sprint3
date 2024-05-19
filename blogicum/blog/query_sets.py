"""Запросы к базе данных."""
from django.utils import timezone

from .models import Category, Post


def posts_query_set():
    """Возвращает список постов."""
    return (
        Post.objects.select_related(
            'category',
            'location',
            'author',
        ).filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True,
        )
    )


def categories_query_set():
    """Возвращает список категорий."""
    return Category.objects.all().filter(is_published=True,)
