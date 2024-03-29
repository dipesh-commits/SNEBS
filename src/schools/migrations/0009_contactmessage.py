# Generated by Django 3.0.5 on 2020-04-27 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0008_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=120, null=True)),
                ('contact_email', models.EmailField(max_length=254, null=True)),
                ('contact_subject', models.CharField(max_length=120, null=True)),
                ('contact_message', models.TextField(null=True)),
                ('timestamps', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
