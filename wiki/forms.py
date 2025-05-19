from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','category','entry']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['entry']