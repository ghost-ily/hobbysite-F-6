from django.db import models

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, related_name='category')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='author')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']