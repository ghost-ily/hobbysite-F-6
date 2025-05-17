from django.contrib import admin
from .models import Thread, ThreadCategory

class PostAdmin(admin.ModelAdmin):
    model = Thread


class PostCategoryAdmin(admin.ModelAdmin):
    model = Thread


# Register your models here.
admin.site.register(Thread, PostAdmin)
admin.site.register(ThreadCategory, PostCategoryAdmin)