from django.contrib import admin
from .models import TodoList
# Register your models here.
class TodolistAdmin(admin.ModelAdmin):
    list_display = ["task","slug","status","started_on","ended_on"]
    list_filter = ["status",]
    prepopulated_fields = {"slug": ["task",]}
    search_fields = ('task',)
    ordering = ('started_on',)

admin.site.register(TodoList, TodolistAdmin)