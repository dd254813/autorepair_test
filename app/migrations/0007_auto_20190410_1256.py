# Generated by Django 2.2 on 2019-04-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_delete_workerschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='time_m',
            field=models.CharField(max_length=5),
        ),
    ]
