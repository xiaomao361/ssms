from django.db import models

# Create your models here.
class Site(models.Model):

    env = (
        ('prod', '正式环境'),
        ('exp', 'example环境'),
        ('test', '测试环境'),
        ('dev', '开发环境'),
    )

    name = models.CharField(
        max_length=50, unique=False, blank=False, verbose_name='站点名称', help_text='站点名称')
    url = models.CharField(
        max_length=50, unique=False, blank=False, verbose_name='地址', help_text='地址')
    description = models.TextField(
        max_length=256,  blank=True, default="", verbose_name='站点描述')
    logo = models.ImageField(upload_to='icon', default='')
    github = models.CharField(
        max_length=50, unique=False, blank=False, default="", verbose_name='源码地址', help_text='源码地址')
    doc = models.CharField(
        max_length=50, unique=False, blank=False, default="", verbose_name='文档地址', help_text='文档地址')
    env = models.CharField(
        max_length=32, choices=env, default="", verbose_name='环境信息')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "站点"
        verbose_name_plural = "站点"