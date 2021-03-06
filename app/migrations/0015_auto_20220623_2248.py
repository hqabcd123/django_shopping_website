# Generated by Django 2.2.27 on 2022-06-23 13:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20220623_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagram',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 22, 48, 48, 773155), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='discuss_borad',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 22, 48, 48, 769164), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='product_borad',
            name='Create_Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 22, 48, 48, 770165), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='history',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user_history_set'),
        ),
    ]
