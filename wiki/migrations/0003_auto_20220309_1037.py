# Generated by Django 3.1.7 on 2022-03-09 10:37

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_auto_20220307_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wiki',
            name='content',
            field=mdeditor.fields.MDTextField(verbose_name='内容'),
        ),
    ]
