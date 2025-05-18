from django.urls import path

from .views import list_threads, PostDetailView, CreateThreadView

urlpatterns = [
    path('forum/threads', list_threads, name='post_list'),
    path('forum/threads/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('forum/threads/add', CreateThreadView.as_view(), name='post_form')
]

app_name='forum'