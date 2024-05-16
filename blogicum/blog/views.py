from django.shortcuts import get_object_or_404, render

from blog.query_sets import get_query_set


def index(request):
    template = 'blog/index.html'
    posts = get_query_set('posts').order_by('-pub_date')[:5]
    return render(request, template, {'post_list': posts})


def post_detail(request, post_id: int):
    template = 'blog/detail.html'
    post = get_object_or_404(
        get_query_set('posts'),
        pk=post_id
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug: str):
    template = 'blog/category.html'
    category = get_object_or_404(
        get_query_set('categories'),
        slug=category_slug
    )
    post_list = (
        get_query_set('posts')
        .filter(category__slug=category_slug)
        .order_by('-pub_date')
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
