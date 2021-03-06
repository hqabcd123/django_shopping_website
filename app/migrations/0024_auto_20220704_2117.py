# Generated by Django 2.2.27 on 2022-07-04 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20220704_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_history',
            name='click_time',
        ),
        migrations.AddField(
            model_name='user_history',
            name='click_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 21, 17, 57, 892986), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='diagram',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 21, 17, 57, 895976), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='discuss_borad',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 21, 17, 57, 890985), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='product_borad',
            name='Create_Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 21, 17, 57, 891986), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='product_code',
            name='product_code',
            field=models.TextField(default='8KHYTAP0GXY5WF0E6AUIMS8JKS1QOLH0', unique=True),
        ),
    ]
