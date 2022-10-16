# Generated by Django 4.1.2 on 2022-10-15 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='weather',
            options={'verbose_name': 'Погода', 'verbose_name_plural': 'Погода'},
        ),
        migrations.AlterField(
            model_name='city',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
