from django.db import models
from django.urls import reverse


class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Thread Categories'
        
    def __str__(self):
        return self.name
        

class Thread(models.Model):
    title = models.CharField(max_length=255)
    entry = models.TextField()
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True
    
    )
    category = models.ForeignKey(
        PostCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='categories'
    )
    
    class Meta:
        ordering = ['-createdOn']
        
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('forum:post_detail', args=[self.pk])
    
