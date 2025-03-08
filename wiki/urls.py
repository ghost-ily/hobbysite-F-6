from django.urls import path
from .views import ArticleCatergoryView, ArticleView

app_name = "wiki"

urlpatterns = [
    path('articles/', ArticleCatergoryView.as_view(), name='category'),
    path('detail/<int:pk>/', ArticleView.as_view(), name='article-detail')
    ]
