from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Language)
class Language(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']


@admin.register(models.Script)
class Script(admin.ModelAdmin):
    list_display = ('alias', 'name', 'language','author', 'c_time')
    search_fields = ['alias']
