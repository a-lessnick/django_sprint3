from django.shortcuts import get_object_or_404, render

from blog.models import Category, Post
from blog.query_sets import category_query_set, posts_query_set


def index(request):
    template = 'blog/index.html'
    posts = posts_query_set().order_by('-pub_date')[:5]
    return render(request, template, {'post_list': posts})


def post_detail(request, post_id: int):
    template = 'blog/detail.html'
    post = get_object_or_404(
        posts_query_set(),
        pk=post_id
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug: str):
    template = 'blog/category.html'
    category = get_object_or_404(category_query_set(), slug=category_slug)
    post_list = (
        posts_query_set()
        .filter(category__slug=category_slug)
        .order_by('-pub_date')
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
