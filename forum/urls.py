from django.urls import path

from .views import PostListView, PostDetailView, CreateThreadView, EditThreadView

urlpatterns = [
    path('forum/threads', PostListView.as_view(), name='post_list'),
    path('forum/threads/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('forum/threads/add', CreateThreadView.as_view(), name='post_form'),
    path('forum/threads/<int:pk>/edit', EditThreadView.as_view(), name='post_edit')
]

app_name='forum'