from django.contrib import admin
from . import models

# Register your models here.

# 后台头标题
admin.site.site_header = 'SSMS'
admin.site.site_title = "SSMS"

# 模型后台注册
@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = ('phone',  'name', 'email',)
    search_fields = ['phone']


@admin.register(models.ExecUser)
class ExecUser(admin.ModelAdmin):
    list_display = ('name',  'username',)
    search_fields = ['name']