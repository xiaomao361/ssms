from django.db import models

# Create your models here.
# 定时任务模型
class CronTask(models.Model):
    # 任务重复类型
    type = (
        ('interval', "interval"),
        ('cron', "cron"),
    )

    name = models.CharField(
        max_length=50, unique=True, blank=False, verbose_name='名称', help_text='名称')
    type = models.CharField(
        max_length=32, choices=type, default="", verbose_name='类型')
    day_of_week = models.CharField(
        max_length=50, unique=False, blank=True, verbose_name='重复日期', help_text='重复日期')
    hour = models.CharField(
        max_length=50, unique=False, blank=True, verbose_name='小时', help_text='小时')  
    minute = models.CharField(
        max_length=50, unique=False, blank=True, verbose_name='分钟', help_text='分钟')
    second = models.CharField(
        max_length=50, unique=False, blank=True, verbose_name='秒', help_text='秒')
    user = models.ForeignKey(
        'member.ExecUser', on_delete=models.CASCADE, default="", verbose_name='执行用户')
    servers = models.ManyToManyField('property.Server', default="", verbose_name='执行服务器')
    script = models.ForeignKey(
        'script.Script', on_delete=models.CASCADE, default="", verbose_name='执行脚本')
    playbook = models.ForeignKey(
        'conf.Conf', on_delete=models.CASCADE, default="", verbose_name='执行剧本')
    is_load = models.BooleanField(default=False, verbose_name='是否加载')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "定时任务"
        verbose_name_plural = "定时任务"