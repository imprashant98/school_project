# Generated by Django 5.0.7 on 2024-07-09 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]
