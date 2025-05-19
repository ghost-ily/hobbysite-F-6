from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, CommentForm

class WikiArticlesView(ListView):
    model = Article
    template_name = 'wiki_list.html'
    context_object_name = 'articles'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ArticleCategory.objects.all()
        return context

class ArticleView(DetailView):
    model = Article
    all = Article.objects.all()
    fields = '__all__'
    template_name = 'wiki_detail.html'
    context = {
              'article': model,
              'articles': all
       }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comment'] = Comment.objects.all()
        return context
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            com = Comment()
            com.author = self.request.user.profile
            com.article = Article.objects.get(pk=article.id)
            com.entry = form.cleaned_data.get('entry')
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
    success_url = 'wiki:article-detail'
    template_name = 'wiki_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ArticleForm()
        return context
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            art = Article()
            art.owner = self.request.user.profile
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
    form_class = ArticleForm
    template_name = 'wiki_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.pk = self.kwargs['pk']
        return context
        
    def form_valid(self, form):
        pk = self.kwargs['pk']
        form.instance.thread = Article.objects.get(pk=pk)
        form.save()
        success_url = reverse_lazy("wiki:article-detail", kwargs={'pk': pk})
        return redirect(success_url)
    
