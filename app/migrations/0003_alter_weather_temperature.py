# Generated by Django 4.1.2 on 2022-10-15 10:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_city_options_alter_weather_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='temperature',
            field=models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(-70), django.core.validators.MaxValueValidator(50)]),
        ),
    ]
