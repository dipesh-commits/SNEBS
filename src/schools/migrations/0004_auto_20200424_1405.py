# Generated by Django 3.0.5 on 2020-04-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_auto_20200424_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.CharField(max_length=90),
        ),
    ]
