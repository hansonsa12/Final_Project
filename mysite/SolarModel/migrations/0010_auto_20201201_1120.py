# Generated by Django 2.2 on 2020-12-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SolarModel', '0009_auto_20201201_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='background_image',
            field=models.ImageField(default='images/space.png', upload_to=''),
        ),
    ]
