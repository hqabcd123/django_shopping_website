# Generated by Django 2.2.27 on 2022-06-27 14:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20220627_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagram',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 27, 23, 19, 35, 80051), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='discuss_borad',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 27, 23, 19, 35, 76048), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='product_borad',
            name='Create_Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 27, 23, 19, 35, 76048), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='product_set',
            name='code',
            field=models.CharField(max_length=32),
        ),
    ]
