# Generated by Django 3.0.5 on 2020-04-25 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_auto_20200424_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='notice_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
