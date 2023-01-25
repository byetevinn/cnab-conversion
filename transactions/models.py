from django.db import models


class Transactions(models.Model):
    type = models.IntegerField(max_length=1)
    date = models.IntegerField(max_length=8)
    value = models.IntegerField(max_length=10)
    cpf = models.IntegerField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.IntegerField(max_length=6)
    store_owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)
