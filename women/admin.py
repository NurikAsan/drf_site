from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'draft']
    list_filter = ('category','draft')