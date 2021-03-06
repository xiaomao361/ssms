# Generated by Django 3.1.7 on 2022-03-08 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0005_auto_20220308_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='名称', max_length=50, verbose_name='名称')),
                ('ip', models.CharField(help_text='IP地址', max_length=50, verbose_name='IP地址')),
                ('ssh_port', models.CharField(help_text='ssh端口', max_length=50, verbose_name='ssh端口')),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('exec_user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='member.execuser', verbose_name='执行用户')),
            ],
            options={
                'verbose_name': '服务器',
                'verbose_name_plural': '服务器',
                'ordering': ['-c_time'],
            },
        ),
    ]
