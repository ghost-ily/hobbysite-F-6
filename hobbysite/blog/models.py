from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ArticleCategory(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Article(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(Profile, on_delete = models.SET_NULL, null = True)
    category = models.ForeignKey(ArticleCategory, on_delete = models.SET_NULL, null = True)
    entry = models.TextField()
    header_image = models.ImageField(upload_to = 'header_images/', null = True, blank=True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article-detail", args={self.pk})

    class Meta:
        ordering = ["-created_on"]

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete = models.SET_NULL, null = True)
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'Comment by {self.author} on {self.article}'

    class Meta:
        ordering = ["created_on"]

