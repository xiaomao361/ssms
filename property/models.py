from django.db import models

# Create your models here.
# 资产模型 - - 目前只针对linux服务
class Server(models.Model):
    name = models.CharField(
        max_length=50, unique=False, blank=False, verbose_name='名称', help_text='名称')
    ip = models.CharField(
        max_length=50, unique=False, blank=False, verbose_name='IP地址', help_text='IP地址')
    ssh_port = models.CharField(
        max_length=50, unique=False, blank=False, verbose_name='ssh端口', help_text='ssh端口')
    exec_user = models.ForeignKey(
        'member.execUser', on_delete=models.CASCADE, default="", verbose_name='执行用户')
    os = models.CharField(
        max_length=50, unique=False, blank=True, verbose_name='操作系统', help_text='操作系统')
    is_online = models.BooleanField(default=False, verbose_name='是否在线')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "服务器"
        verbose_name_plural = "服务器"