from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.

# 语言模型
class Language(models.Model):
    name = models.CharField(
        max_length=50, unique=False, blank=False, verbose_name='语言', help_text='语言')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "语言"
        verbose_name_plural = "语言"


# 脚本模型
class Script(models.Model):
    alias = models.CharField(
        max_length=50, unique=False, blank=False, verbose_name='别名', help_text='别名')
    name = models.CharField(
        max_length=50, unique=False, blank=False, verbose_name='名称', help_text='名称')
    content = MDTextField(verbose_name='内容')
    language = models.ForeignKey(
        'language', on_delete=models.CASCADE, default="", verbose_name='语言')
    author = models.ForeignKey(
        'member.user', on_delete=models.CASCADE, default="", verbose_name='作者')
    note = models.CharField(
        max_length=50, unique=False, blank=True, verbose_name='备注', help_text='备注')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.alias

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "脚本"
        verbose_name_plural = "脚本"
