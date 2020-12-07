# Generated by Django 2.2 on 2020-11-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SolarModel', '0002_auto_20201126_1013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planet',
            old_name='planet_attributes',
            new_name='planet_characteristics',
        ),
        migrations.RenameField(
            model_name='planet',
            old_name='planet_location',
            new_name='planet_distance',
        ),
        migrations.AddField(
            model_name='planet',
            name='planet_age',
            field=models.CharField(default='default', max_length=200),
        ),
        migrations.AddField(
            model_name='planet',
            name='planet_mass',
            field=models.CharField(default='default', max_length=200),
        ),
    ]