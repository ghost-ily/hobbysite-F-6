from django import forms
from .models import Thread, ThreadCategory, Comment


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'entry', 'category']