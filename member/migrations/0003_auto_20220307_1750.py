# Generated by Django 3.1.7 on 2022-03-07 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20220307_1045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-c_time'], 'verbose_name': '姓名', 'verbose_name_plural': '用户信息'},
        ),
    ]
