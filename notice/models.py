from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.
# 消息类型
class Notice(models.Model):
    title = models.CharField(
        max_length=50, unique=False, blank=False, verbose_name='通知标题', help_text='通知标题')
    content = MDTextField(verbose_name='内容')
    is_read = models.BooleanField(default=False, verbose_name='是否已读')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "系统通知"
        verbose_name_plural = "系统通知"
        get_latest_by = "c_time"


# 消息模型
class Message(models.Model):
    sender = models.ForeignKey(
        'member.user', on_delete=models.CASCADE, default="", verbose_name='发送人', related_name='sender')
    receiver = models.ForeignKey(
        'member.user', on_delete=models.CASCADE, default="", verbose_name='接收人', related_name='receiver')
    subject = models.CharField(
        max_length=50, unique=False, blank=False, verbose_name='主题', help_text='主题')
    content = models.TextField(
        max_length=250, unique=False, blank=False, verbose_name='内容', help_text='内容')
    is_read = models.BooleanField(default=False, verbose_name='是否已读')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "消息"
        verbose_name_plural = "消息"
        get_latest_by = "c_time"