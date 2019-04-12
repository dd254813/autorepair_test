# Generated by Django 2.2 on 2019-04-10 10:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 4, 10, 10, 33, 50, 977397, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='time',
            field=models.TimeField(default=datetime.datetime(2019, 4, 10, 10, 33, 58, 81392, tzinfo=utc)),
            preserve_default=False,
        ),
    ]