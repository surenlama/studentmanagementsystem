# Generated by Django 2.1 on 2020-08-08 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200808_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='studentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='studentphone',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='studentrollno',
            field=models.IntegerField(default=0),
        ),
    ]
