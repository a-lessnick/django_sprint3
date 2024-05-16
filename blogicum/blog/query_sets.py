from django.utils import timezone

from .models import Category, Post


def get_query_set(query_set_name):
    date_now = timezone.now()

    if query_set_name == 'posts':
        query_set = (
            Post.objects.select_related(
                'category',
                'location',
                'author',
            ).only(
                'title',
                'text',
                'pub_date',
                'author__username',
                'category__title',
                'category__slug',
                'location__name',
            ).filter(
                pub_date__lte=date_now,
                is_published=True,
                category__is_published=True,
            )
        )

    elif query_set_name == 'categories':
        query_set = (
            Category.objects.values(
                'title',
                'description',
            ).filter(
                is_published=True,
            )
        )

    return query_set
