# Generated by Django 2.2 on 2022-04-18 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0025_auto_20220417_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allgroups',
            name='sessionKey',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='sessionKey',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='sessionKey',
        ),
    ]
