from django.db import models

class Question(models.Model):
    id_tovara = models.IntegerField(default=0)
    id_postav = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    kol_vo = models.IntegerField(default=0)
    cena = models.IntegerField(default=0)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)