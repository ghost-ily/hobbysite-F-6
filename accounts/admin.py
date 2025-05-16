from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile

class ProfileInline(admin.StackedInline):
    models = Profile
    can_delete = True
    
    
class UserAdmin(admin.UserAdmin):
    inlines = [ProfileInline]
    
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
