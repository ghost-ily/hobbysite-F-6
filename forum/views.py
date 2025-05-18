from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import ThreadCategory, Thread, Comment
from .forms import ThreadForm, CommentForm


class PostListView(ListView):
    model = ThreadCategory
    template_name = 'post_list.html'


class CreateThreadView(CreateView):
    form_class = ThreadForm
    success_url = 'forum:post_list'
    template_name = 'post_form.html'


class PostDetailView(DetailView):
    model = Thread
    template_name = 'post_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
        
    def post(self, request, *args, **kwargs):
        thread_pk = self.kwargs['pk']
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.entry = form.cleaned_data.get('entry')
            comment.thread = Thread.objects.get(pk=thread_pk)
            comment.save()
        success_url = reverse_lazy("forum:post_detail", kwargs={'pk':thread_pk})
        return redirect(success_url)
