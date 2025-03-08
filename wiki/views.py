from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ArticleCategory, Article

class ArticleCatergoryView(ListView):
    model = Article
    template_name = 'wiki_list.html'
    context_object_name = 'articles'

class ArticleView(DetailView):
    model = Article
    template_name = 'wiki_detail.html'
    context_object_name = 'article'
