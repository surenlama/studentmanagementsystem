# Generated by Django 2.1 on 2020-08-08 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20200808_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='studentage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='studentemail',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='studentname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='studentphone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='studentrollno',
            field=models.IntegerField(),
        ),
    ]
