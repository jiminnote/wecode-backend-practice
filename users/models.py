from django.db import models

from core.models      import TimeStampModel

class User(TimeStampModel):   
    first_name      = models.CharField(max_length=45)
    last_name       = models.CharField(max_length=45)
    email           = models.CharField(max_length=45,unique=True)
    password        = models.CharField(max_length=200)
    skin_type       = models.ForeignKey("Skintype",on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'users'
        
    def __str__(self):
            return self.last_name + self.first_name
        
class Skintype(models.Model):
    skin_type = models.CharField(max_length=15,null=True)
    
    class Mete:
        db_table = 'skin_types'
        

    


