from django import forms
from django.db import models
from django.contrib import admin
from .models import Documents, Tasks, User, Token, UserTasks

@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_email', 'file_url')
    search_fields = ('user__email',)
    list_filter = ('user__email',)

    def user_email(self, obj):
        return obj.user.email

    def file_url(self, obj):
        return obj.theFile.url

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'amounts', 'title', 'description')
    search_fields = ('title',)
    formfield_overrides = {
        models.FloatField: {'widget': forms.NumberInput(attrs={'step': '0.1'})},
    }

@admin.register(UserTasks)
class UserTasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_title', 'status', 'created_at', 'user_email')
    search_fields = ('task__title', 'user__email')
    list_filter = ('status', 'task__title', 'user__email', 'created_at')

    def task_title(self, obj):
        return obj.task.title

    def user_email(self, obj):
        return obj.user.email

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'earned', 'is_verify')
    search_fields = ('email',)
    list_filter = ('is_verify', 'earned')
    
@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user_email')
    search_fields = ('user__email',)

    def user_email(self, obj):
        return obj.user.email



