# Generated by Django 2.2 on 2022-04-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0017_auto_20220416_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='respondentID',
        ),
        migrations.AddField(
            model_name='doctor',
            name='numberOfVisits',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='allgroups',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='general',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
