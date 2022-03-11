# Generated by Django 3.1.7 on 2022-03-11 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0005_auto_20220308_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='消息类型', max_length=50, verbose_name='消息类型')),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '消息类型',
                'verbose_name_plural': '消息类型',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(help_text='主题', max_length=50, verbose_name='主题')),
                ('content', models.TextField(help_text='内容', max_length=250, verbose_name='内容')),
                ('is_read', models.BooleanField(default=False, verbose_name='是否已读')),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='member.user', verbose_name='接收人')),
                ('sender', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='member.user', verbose_name='发送人')),
                ('type', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='notice.type', verbose_name='消息类型')),
            ],
            options={
                'verbose_name': '消息',
                'verbose_name_plural': '消息',
                'ordering': ['-c_time'],
                'get_latest_by': 'c_time',
            },
        ),
    ]
