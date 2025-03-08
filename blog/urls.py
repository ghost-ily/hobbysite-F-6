from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('blog/articles', BlogListView.as_view(), name = 'article-list'),
    path('blog/article/<int:pk>', BlogDetailView.as_view(), name = 'article-detail')
]