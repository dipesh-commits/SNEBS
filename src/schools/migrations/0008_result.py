# Generated by Django 3.0.5 on 2020-04-26 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0007_boardofdirector'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_title', models.CharField(max_length=120, null=True)),
                ('result_file', models.FileField(null=True, upload_to='')),
                ('timestamps', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
