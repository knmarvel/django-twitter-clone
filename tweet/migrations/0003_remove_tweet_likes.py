# Generated by Django 3.0.6 on 2020-05-28 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_auto_20200527_0203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='likes',
        ),
    ]