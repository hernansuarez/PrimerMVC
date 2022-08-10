from wsgiref.handlers import format_date_time
from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    estatura = models.FloatField()
    fecha_nacimiento = models.DateField(format_date_time)