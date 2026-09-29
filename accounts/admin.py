from django.contrib import admin

# Register your models here.

from .models import UserProfile, NGOProfile

admin.site.register(UserProfile)
admin.site.register(NGOProfile)