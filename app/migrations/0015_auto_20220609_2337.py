# Generated by Django 2.2.27 on 2022-06-09 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20220607_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='image_album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='diagram',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 23, 37, 35, 919228), help_text='create date: '),
        ),
    ]
