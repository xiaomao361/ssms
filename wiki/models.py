from aioredis import AuthError
from django.db import models
from ckeditor.fields import RichTextField
from mdeditor.fields import MDTextField


# Create your models here.


# 类型模型
class Category(models.Model):
    type = models.CharField(
        max_length=50, unique=False, blank=False, verbose_name='类目', help_text='类目')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "类目"
        verbose_name_plural = "类目"


# 文本模型
class Wiki(models.Model):
    title = models.CharField(
        max_length=50, unique=False, blank=False, verbose_name='标题', help_text='标题')
    # content = RichTextField(verbose_name='内容')
    content = MDTextField(verbose_name='内容')
    category = models.ForeignKey(
        'category', on_delete=models.CASCADE, default="", verbose_name='类目')
    author = models.ForeignKey(
        'member.user', on_delete=models.CASCADE, default="", verbose_name='作者')
    number = models.IntegerField(
        unique=False, blank=False, default=0, verbose_name='阅读次数', help_text='阅读次数')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "文章"
        verbose_name_plural = "文章"
