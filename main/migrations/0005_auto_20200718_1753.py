# Generated by Django 2.2.6 on 2020-07-18 17:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200718_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='display_name',
            field=models.CharField(default=datetime.datetime(2020, 7, 18, 17, 53, 10, 427184, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='popularity',
            field=models.IntegerField(),
        ),
    ]
