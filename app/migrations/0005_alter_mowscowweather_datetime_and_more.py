# Generated by Django 4.1.2 on 2022-10-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_mowscowweather_remove_weather_city_delete_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mowscowweather',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, unique=True),
        ),
        migrations.AlterModelTable(
            name='mowscowweather',
            table='weather',
        ),
    ]
