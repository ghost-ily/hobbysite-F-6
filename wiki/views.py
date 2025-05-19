from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, CommentForm

class ArticleCatergoryView(ListView):
    model = Article
    template_name = 'wiki_list.html'
    context_object_name = 'articles'

class ArticleView(DetailView):
    model = Article
    fields = '__all__'
    template_name = 'wiki_detail.html'
    context_object_name = 'thisarticle'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            com = Comment()
            com.author = self.request.user.profile
            com.entry= Article.objects.get(pk=article_pk)
            com.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = '__all__'
    template_name = 'wiki_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ArticleForm()
        return context
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            art = Article()
            art.title = form.cleaned_data.get('title')
            art.category = form.cleaned_data.get('category')
            art.entry= form.cleaned_data.get('entry')
            art.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'wiki_update.html'
    
