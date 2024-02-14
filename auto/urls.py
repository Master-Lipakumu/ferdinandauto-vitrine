from django.urls import path

from .views import (articles_list, article_detail, search_articles,
                     contact_view, contact_success_view)


urlpatterns = [
    path('', articles_list, name='articles_list'),
    path('articles/search/', search_articles, name='search_articles'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success_view, name='contact_success'),
]
