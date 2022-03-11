from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Notice)
class Notice(admin.ModelAdmin):
    list_display = ('title',  'c_time',)
    search_fields = ['title']


@admin.register(models.Message)
class Message(admin.ModelAdmin):
    list_display = ('subject', 'is_read', 'c_time')
    search_fields = ['subject']
