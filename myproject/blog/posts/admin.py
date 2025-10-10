from django.contrib import admin
from .models import Category, Topic

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'created')
    list_filter = ('category',)
    search_fields = ('name',)
