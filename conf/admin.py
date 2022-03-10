from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Type)
class Type(admin.ModelAdmin):
    list_display = ('name',  'c_time',)
    search_fields = ['name']


@admin.register(models.Conf)
class Conf(admin.ModelAdmin):
    list_display = ('alias', 'name', 'author', 'c_time')
    search_fields = ['name']