# Generated by Django 3.1.7 on 2022-03-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_auto_20220311_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='是否已读'),
        ),
    ]