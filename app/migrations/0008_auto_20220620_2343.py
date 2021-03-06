# Generated by Django 2.2.27 on 2022-06-20 14:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20220620_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_borad',
            name='product_type',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='app.product_type'),
        ),
        migrations.AlterField(
            model_name='diagram',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 23, 43, 7, 217056), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='discuss_borad',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 23, 43, 7, 215055), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='product_borad',
            name='Create_Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 20, 23, 43, 7, 216055), help_text='create date: '),
        ),
    ]
