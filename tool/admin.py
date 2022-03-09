from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Site)
class Site(admin.ModelAdmin):
    list_display = ('name', 'description', 'env')
    search_fields = ['name']