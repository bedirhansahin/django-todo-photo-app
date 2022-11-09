from django.contrib import admin
from . models import Todo, Photo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['user', 'todo', 'status', 'create_date', 'due_date']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'publish_date']
