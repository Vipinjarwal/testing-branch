from django.db import models

# Create your models here.


class Crypto(models.Model):
    coin_name = models.CharField(max_length=200)
    coin_price = models.IntegerField()
    coin_exchange = models.CharField(max_length=200)
        
        
