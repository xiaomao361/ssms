from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.CronTask)
class CronTask(admin.ModelAdmin):
    list_display = ('name',  'type', 'script', 'playbook', 'is_load')
    search_fields = ['name']