from django.urls import path
from .views import ArticleCatergoryView, ArticleView, ArticleCreateView, ArticleUpdateView

app_name = 'wiki'

urlpatterns = [
    path('wiki/articles/', ArticleCatergoryView.as_view(), name='category'),
    path('wiki/article/<int:pk>/', ArticleView.as_view(), name='article-detail')
    path('wiki/article/add/', ArticleCreateView.as_view(), name='article-create')
    path('wiki/article/<int:pk>/edit', ArticleUpdateView.as_view(), name='article-update')
    ]
