# Generated by Django 3.0.5 on 2020-04-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0005_notice_notice_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=120, null=True)),
                ('teacher_designation', models.CharField(max_length=120, null=True)),
                ('teacher_image', models.ImageField(null=True, upload_to='')),
                ('timestamps', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]