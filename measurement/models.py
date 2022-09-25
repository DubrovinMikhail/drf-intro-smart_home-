# class PostMeasurement()


from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя датчика')
    description = models.CharField(max_length=250, blank=True,  verbose_name='Описание')


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
