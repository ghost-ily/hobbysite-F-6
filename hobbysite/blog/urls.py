from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, CommentCreateView

urlpatterns = [
    path('blog/articles', BlogListView.as_view(), name = 'article-list'),
    path('blog/article/<int:pk>', BlogDetailView.as_view(), name = 'article-detail'),
    path('blog/article/add', BlogCreateView.as_view(), name='article-create'),
    path('blog/article/<int:pk>/edit', BlogUpdateView.as_view(), name='article-update'),
    path('blog/article/<int:pk>/comment/add', CommentCreateView.as_view(), name='comment-create'),
]