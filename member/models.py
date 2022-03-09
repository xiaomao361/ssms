from django.db import models
import hashlib
from ckeditor.fields import RichTextField


# Create your models here.
# 用户模型
class User(models.Model):

    # 选择器
    genders = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(
        max_length=50, blank=False, verbose_name='姓名', help_text='姓名')
    gender = models.CharField(
        max_length=32, choices=genders, default="", verbose_name='性别')
    phone = models.CharField(
        max_length=50, unique=True,  blank=False, verbose_name='电话', help_text='电话')
    email = models.CharField(
        max_length=50, blank=False, verbose_name='邮箱', help_text='邮箱')
    password = models.CharField(
        max_length=50, blank=False, verbose_name='密码', help_text='密码')
    icon = models.ImageField(upload_to='icon', default='icon/default.jpg')

    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "姓名"
        verbose_name_plural = "用户信息"

    def save(self, *args, **kwargs):
        md5 = hashlib.md5()
        md5.update(self.password.encode())
        self.password = md5.hexdigest()
        super(User, self).save(*args, **kwargs)

class ExecUser(models.Model):
    name = models.CharField(
        max_length=50, blank=False, verbose_name='名称', help_text='名称')
    username = models.CharField(
        max_length=50, blank=False, verbose_name='用户名', help_text='用户名')
    password = models.CharField(
        max_length=50, blank=True, verbose_name='密码', help_text='密码')
    sshkey = models.FileField(upload_to='sshkey', blank=True, default='')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "名称"
        verbose_name_plural = "执行用户"

    def save(self, *args, **kwargs):
        if self.password:
            md5 = hashlib.md5()
            md5.update(self.password.encode())
            self.password = md5.hexdigest()
            super(ExecUser, self).save(*args, **kwargs)
        else:
            super(ExecUser, self).save(*args, **kwargs)
