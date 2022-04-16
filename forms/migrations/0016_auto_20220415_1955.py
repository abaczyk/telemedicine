# Generated by Django 2.2 on 2022-04-15 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0015_auto_20220415_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allgroups',
            name='respondentID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forms.General'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='respondentID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forms.General'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='respondentID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forms.General'),
        ),
    ]