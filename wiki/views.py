from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from .models import ArticleCategory, Article

class ArticleCatergoryView(ListView):
    model = Article
    template_name = 'wiki_list.html'
    context_object_name = 'articles'

class ArticleView(DetailView):
    model = Article
    template_name = 'wiki_detail.html'
    context_object_name = 'article'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'wiki_create.html'
    context_object_name = 'article'

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'wiki_update.html'
    context_object_name = 'article'
