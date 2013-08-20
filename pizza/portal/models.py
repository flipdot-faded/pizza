from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    pass

class Order(models.Model):
    user = models.ForeignKey(User)
    items = models.ManyToManyField(Item)


    def price(self):
        return 0
