# Generated by Django 3.1.6 on 2021-03-08 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='content',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='date_updated',
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
