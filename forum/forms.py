from django import forms
from .models import Thread, ThreadCategory, Comment


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'entry', 'category']
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
        labels = {
            "entry": "Comment"
        }