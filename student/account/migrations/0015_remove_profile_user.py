# Generated by Django 2.1 on 2020-08-08 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20200808_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
