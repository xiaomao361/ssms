from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = ('id',  'type')
    search_fields = ['type']


@admin.register(models.Wiki)
class Wiki(admin.ModelAdmin):
    list_display = ('title',  'author', 'c_time')
    search_fields = ['title']