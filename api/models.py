from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Test(models.Model):
    login = models.CharField(max_length=10, verbose_name="Идентификатор", unique=True)
    iq_time = models.DateTimeField(verbose_name="Время IQ", blank=True, null=True)
    iq_points = models.PositiveIntegerField(verbose_name="Баллы", blank=True, null=True, validators=[
            MinValueValidator(0),
            MaxValueValidator(50)
        ])
    eq_time = models.DateTimeField(verbose_name="Время EQ", blank=True, null=True)
    eq_result = ArrayField(models.CharField(max_length=1), size=5, verbose_name="Результат", blank=True, null=True)

