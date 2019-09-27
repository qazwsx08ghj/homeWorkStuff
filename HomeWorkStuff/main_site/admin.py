from django.contrib import admin

# Register your models here.
from main_site.models import userProfile ,userArticle

admin .site.register(userProfile)
admin .site.register(userArticle)