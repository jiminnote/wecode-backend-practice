from tkinter import CASCADE
from django.db import models
from core import TimeStampModel

# Create your models here.
class Cart(models.Model):
    products_count    = models.IntegerField(max_length=50)
    user_id           = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product_option_id = models.TextField()
    
    class Meta:
     db_table='products'
     
class Order(TimeStampModel):
    order_number = models.CharField(max_length=50)
    user_id      = models.ForeignKey("users.User", on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address      = models.CharField(max_length=100)
    status_id    = models.ForeignKey("Status", on_delete=models.CASCADE)
    
    class Meta:
     db_table='orders'
    
    def __str__(self):
        return self.order_number

class Status(models.Model):
    status = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'statuses'
        
class Order_item(models.Model):
    order_id          = models.ForeignKey("Order", on_delete=models.CASCADE)
    product_option_id = models.ForeignKey("product.Product", on_delete = models.CASCADE)
    product_count     = models.IntegerField(max_length=100)
    
    class Mta:
        db_table = 'order_itmes'
    
    