from django.db import models
from core      import TimeStampModel

# Create your models here.
class Main_Category(models.Model):
    name=models.CharField(max_length=50)
    
    class Meta:
     db_table='main_categories'
     
    def __str__(self):
            return self.main_categories_name
        
class Sub_category(models.Model):
    sub_category_name = models.CharField(max_length=50)
    Main_Category     = models.ForeignKey("Main_category",on_delete=models.CASCADE)
    
    class Meta:
     db_table='sub_categories'
     
class Product(TimeStampModel):
    sub_category      = models.ForeignKey('Sub_categories', on_delete=models.CASCADE)
    products_name     = models.CharField(max_length=50)
    products_contents = models.TextField()
    
    class Meta:
     db_table='products'

class Product_option(TimeStampModel):
    products_id      = models.ForeignKey('Product', on_delete=models.CASCADE)
    sizes_mL         = models.CharField(max_length=20)
    products_img_url = models.URLField()
    price            = models.DecimalField(max_length=20)
    include_pump     = models.BooleanField()
    size_contents    = models.TextField()
    
    class Meta:
         db_table='product_options'

class Products_feature(TimeStampModel):
    products_id  = models.ForeignKey("Products",related_name='Products_feature', on_delete=models.CASCADE)    
    features_id  = models.ForeignKey("Feature", on_delete=models.CASCADE)  
    contents     = models.TextField()
    
    class Meta:
         db_table='products_features'
         

class Feature(TimeStampModel):
    features_name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'features'

class Recommend_product(TimeStampModel):
    products_id = models.ForeignKey("Products", related_name='recommend_products', on_delete=models.CASCADE)   
    
    class Meta:
        db_table = 'recommend_products'