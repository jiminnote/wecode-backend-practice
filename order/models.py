from django.db import models

from core.models import TimeStampModel

# Create your models here.
class Cart(models.Model):
    quantity       = models.IntegerField()
    user           = models.ForeignKey("users.User", on_delete = models.CASCADE)
    product_option = models.ForeignKey("product.Productoption", on_delete = models.CASCADE)
    
    class Meta:
        db_table = 'carts'
     
class Order(TimeStampModel):
    order_number = models.CharField(max_length = 50)
    user         = models.ForeignKey("users.User", on_delete = models.CASCADE)
    phone_number = models.CharField(max_length = 20)
    address      = models.CharField(max_length = 100)
    status       = models.ForeignKey("Status", on_delete = models.CASCADE)
    
    class Meta:
        db_table = 'orders'
    
    def __str__(self):
        return self.order_number

class Status(models.Model):
    status = models.CharField(max_length = 20)
    
    class Meta:
        db_table = 'statuses'
        
class Orderitem(models.Model):
    order          = models.ForeignKey("Order", on_delete = models.CASCADE)
    product_option = models.ForeignKey("product.Product", on_delete = models.CASCADE)
    quantity       = models.IntegerField()
    
    class Meta:
        db_table = 'order_itmes'
    
    