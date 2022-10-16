from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django_cte import CTEManager


class MoscowWeather(models.Model):
    objects = CTEManager()
    date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True, unique=True)
    temperature = models.FloatField(validators=[MinValueValidator(-70), MaxValueValidator(50)])

    class Meta:
        verbose_name = 'Погода'
        verbose_name_plural = verbose_name
        db_table = 'weather'

    def __str__(self):
        return 'Moscow' + '__' + str(self.datetime)
