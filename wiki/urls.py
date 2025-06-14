from django.urls import path
from .views import WikiArticlesView, ArticleView, ArticleCreateView, ArticleUpdateView

app_name = 'wiki'

urlpatterns = [
    path('articles/', WikiArticlesView.as_view(), name='category'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article-detail'),
    path('article/add/', ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/edit', ArticleUpdateView.as_view(), name='article-update')
    ]
