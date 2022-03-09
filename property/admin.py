from django.contrib import admin
from . import models


# Register your models here.
# 模型后台注册
@admin.register(models.Server)
class Server(admin.ModelAdmin):
    list_display = ('name',  'ip', 'ssh_port', 'exec_user', 'os', 'is_online')
    search_fields = ['name']