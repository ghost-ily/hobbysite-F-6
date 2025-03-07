from django.urls import path

from .views import PostListView, PostDetailView

urlpatterns = [
    path('posts/list', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail')
]

app_name='forum'