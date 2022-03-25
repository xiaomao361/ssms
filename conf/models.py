from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.
# 配置模型
class Type(models.Model):
    name = models.CharField(
        max_length=50, unique=False, blank=False, verbose_name='配置类型', help_text='配置类型')
    extension = models.CharField(
        max_length=50, unique=False, blank=True, verbose_name='后缀名', help_text='后缀名')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "配置类型"
        verbose_name_plural = "配置类型"


# 配置模型
class Conf(models.Model):
    alias = models.CharField(
        max_length=50, unique=False, blank=False, verbose_name='别名', help_text='别名')
    name = models.CharField(
        max_length=50, unique=False, blank=False, verbose_name='名称', help_text='名称')
    content = MDTextField(verbose_name='内容')
    type = models.ForeignKey(
        'type', on_delete=models.CASCADE, default="", verbose_name='类型')
    author = models.ForeignKey(
        'member.user', on_delete=models.CASCADE, default="", verbose_name='作者')
    note = models.CharField(
        max_length=50, unique=False, blank=True, verbose_name='备注', help_text='备注')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.alias

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "配置文件"
        verbose_name_plural = "配置文件"

