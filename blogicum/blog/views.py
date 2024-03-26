from datetime import datetime as dt
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from blog.models import Category, Post


def get_related_post_list():
    """Функция возвращает объекты модели Post со связанными моделями."""
    return Post.objects.select_related(
        'category', 'location', 'author')


def index(request: HttpRequest) -> HttpResponse:
    """Функция отображает главную страницу"""
    post_list = get_related_post_list().filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=dt.now()
    )[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    """Функция отображает отдельную публикацию"""
    post = get_object_or_404(
        get_related_post_list(),
        is_published=True,
        pub_date__lte=dt.now(),
        category__is_published=True,
        pk=post_id
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    """Функция отображает публикации в категории"""
    post_list = get_list_or_404(
        Post,
        is_published=True,
        category__slug=category_slug,
        pub_date__lte=dt.now()
    )
    category = get_object_or_404(
        Category,
        is_published=True,
        slug=category_slug
    )
    context: dict = {'category': category,
                     'post_list': post_list}
    return render(request, 'blog/category.html', context)
