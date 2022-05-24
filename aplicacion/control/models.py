from django.db import models


class MovimientoRectilineo (models.Model):
    distanica = models.IntegerField()
    tiempo = models.FloatField()
    Angulo = models.IntegerField()
