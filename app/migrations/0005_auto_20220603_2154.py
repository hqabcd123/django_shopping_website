# Generated by Django 2.2.27 on 2022-06-03 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220603_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagram',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 3, 21, 54, 24, 779235), help_text='create date: '),
        ),
    ]