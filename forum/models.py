from django.db import models
from django.urls import reverse


class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
        

class Post(models.Model):
    title = models.CharField(max_length=255)
    entry = models.TextField()
    createdOn = models.DateTimeField()
    updatedOn = models.DateTimeField()
    category = models.ForeignKey(
        PostCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='categories'
    )
    
    class Meta:
        ordering = ['-createdOn']
        
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('forum:post_detail', args=[self.pk])
    
