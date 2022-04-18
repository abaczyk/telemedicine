# Generated by Django 2.2 on 2022-04-17 16:50

from django.db import migrations, models
import django.db.models.deletion
import forms.models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0019_auto_20220417_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allgroups',
            name='respondentID',
            field=models.OneToOneField(default=forms.models.default_general, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.General'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='respondentID',
            field=models.OneToOneField(default=forms.models.default_general, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.General'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='respondentID',
            field=models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.General'),
        ),
    ]