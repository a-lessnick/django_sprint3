""" Функции отображения данных для передачи в шаблоны."""
from django.shortcuts import get_object_or_404, render

from blog.models_constants import POSTS_ON_INDEX
from blog.query_sets import get_query_set


def index(request):
    """
    Главная страница приложения blog.
    :param request:
    :return: render объект
    """
    template = 'blog/index.html'
    posts = get_query_set('posts')[:POSTS_ON_INDEX]
    return render(request, template, {'post_list': posts})


def post_detail(request, post_id: int):
    """
    Отдельный пост.
    :param request:
    :param post_id: идентификатор поста
    :return: render объект
    """
    template = 'blog/detail.html'
    post = get_object_or_404(
        get_query_set('posts'),
        pk=post_id
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug: str):
    """
    Перечень постов в категории.
    :param request:
    :param category_slug: slug категории
    :return: render объект
    """
    template = 'blog/category.html'
    category = get_object_or_404(
        get_query_set('categories'),
        slug=category_slug
    )
    post_list = (
        get_query_set('posts')
        .filter(category=category)
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
