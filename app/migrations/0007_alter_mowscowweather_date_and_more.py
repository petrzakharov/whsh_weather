# Generated by Django 4.1.2 on 2022-10-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_mowscowweather_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mowscowweather',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='mowscowweather',
            name='datetime',
            field=models.DateTimeField(unique=True),
        ),
    ]
