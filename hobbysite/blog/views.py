from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article, ArticleCategory, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from .forms import ArticleForm, CommentForm

class BlogListView(ListView):
    model = ArticleCategory
    context_object_name = 'articlecategories'
    template_name = 'article_list.html'

class BlogDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        article = form.save()
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'update_article.html'

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'
    success_url = reverse_lazy('article-list')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        form.instance.article = Article.objects.get(pk=self.kwargs['pk'])
        comment = form.save()
        return super().form_valid(form)
