from django.db        import models

from core.models      import TimeStampModel

# Create your models here.
class MainCategory(models.Model):
    name = models.CharField(max_length = 50)
    
    class Meta:
        db_table = 'main_categories'
     
    def __str__(self):
        return self.name
        
class Subcategory(models.Model):
    name          = models.CharField(max_length = 50)
    main_category = models.ForeignKey("Maincategory",on_delete = models.CASCADE)
    
    class Meta:
        db_table = 'sub_categories'
     
class Product(TimeStampModel):
    sub_category         = models.ForeignKey('Subcategory', on_delete = models.CASCADE)
    name                 = models.CharField(max_length = 50)
    content              = models.TextField()
    additional_image_url = models.URLField()
    
    class Meta:
        db_table = 'products'

class Productoption(TimeStampModel):
    product          = models.ForeignKey('Product', on_delete = models.CASCADE)
    sizes_mL         = models.CharField(max_length = 20)
    image_url        = models.URLField()
    price            = models.DecimalField(max_digits = 10, decimal_places = 3)
    is_include_pump  = models.BooleanField(default = False)
    content          = models.TextField()
    
    class Meta:
        db_table = 'product_options'

class Productfeature(models.Model):
    product      = models.ForeignKey("Product", related_name = 'Products_feature', on_delete = models.CASCADE)    
    feature      = models.ForeignKey("Feature", on_delete = models.CASCADE) 
    is_addtional = models.BooleanField(default = False)
    content      = models.TextField()
    
    class Meta:
        db_table = 'products_features'
         

class Feature(TimeStampModel):
    name = models.CharField(max_length = 50)
    
    class Meta:
        db_table = 'features'

class Recommend(TimeStampModel):
    reference_product = models.ForeignKey("Product", related_name = 'recommend_products', on_delete = models.CASCADE)
    recommend_product = models.ForeignKey("Product", related_name = 'reference_products', on_delete = models.CASCADE)   
    
    class Meta:
        db_table = 'recommend_products'