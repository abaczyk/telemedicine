# Generated by Django 2.2 on 2022-04-14 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20220414_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usePOZ', models.BooleanField()),
                ('freqOfVisits', models.CharField(max_length=100)),
                ('isPunctual', models.BooleanField()),
                ('correctDateOfEConsultation', models.BooleanField()),
                ('respondentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.General')),
            ],
        ),
    ]