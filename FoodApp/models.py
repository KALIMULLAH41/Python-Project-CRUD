from django.db import models

# Create your models here.
class Items(models.Model):
    #def __str__(self):
    #  return self.item_name
    item_name=models.CharField(max_length=122)
    item_desc=models.CharField(max_length=122)
    item_price=models.IntegerField()
