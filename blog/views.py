from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article, ArticleCategory

class BlogListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'article_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        print("Articles being passed to the template:", queryset)  # Debugging
        return queryset

class BlogDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article_detail.html'
