from django.urls import path
from django.views.decorators.cache import cache_page
from .views import (
    New, News, Search, ArticlesPostCreate, NewsPostCreate, ArticlesPostUpdate,
    NewsPostUpdate, ArticlesPostDelete, NewsPostDelete, CategoryListView, subscribe
)

urlpatterns = [
    path('', News.as_view(), name='news'),
    path('<int:pk>', New.as_view(), name='new'),
    path('search/', Search.as_view(), name='search'),
    path('articles/create/', ArticlesPostCreate.as_view(), name='articles_post_create'),
    path('news/create/', NewsPostCreate.as_view(), name='news_post_create'),
    path('articles/<int:pk>/update/', ArticlesPostUpdate.as_view(), name='articles_post_update'),
    path('news/<int:pk>/update/', NewsPostUpdate.as_view(), name='news_post_update'),
    path('articles/<int:pk>/delete/', ArticlesPostDelete.as_view(), name='articles_post_delete'),
    path('news/<int:pk>/delete/', NewsPostDelete.as_view(), name='news_post_delete'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]
