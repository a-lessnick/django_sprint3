"""
Запросы к базе данных.
"""
from django.utils import timezone

from .models import Category, Post


def get_query_set(query_set_name: str):
    """
    Возвращает результат запроса к БД в зависимости от имени QuerySet.
    :param query_set_name: имя запроса
    :return: соответствующий QuerySet объект
    """

    if query_set_name == 'posts':
        query_set = (
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

    elif query_set_name == 'categories':
        query_set = (
            Category.objects.all().filter(is_published=True,)
        )

    return query_set
