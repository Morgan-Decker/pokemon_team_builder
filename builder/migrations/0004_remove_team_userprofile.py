# Generated by Django 3.1.7 on 2021-04-03 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0003_auto_20210403_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='userprofile',
        ),
    ]
