from django.db import models

# Create your models here.
class Items(models.Model):
    #def __str__(self):
    #  return self.item_name
    item_name=models.CharField(max_length=122)
    item_desc=models.CharField(max_length=122)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=5000,default='https://img.freepik.com/premium-vector/loading-icon_167801-436.jpg?w=360')