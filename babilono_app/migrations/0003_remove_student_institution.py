# Generated by Django 2.0.1 on 2018-01-23 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('babilono_app', '0002_auto_20180123_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='institution',
        ),
    ]
