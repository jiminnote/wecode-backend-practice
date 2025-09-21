

from django.db              import models
from validation             import *
from django.forms import ModelForm

class User(models.Model):
    first_name   =models.CharField(max_length=50,validators=[validate_name])
    last_name    =models.CharField(max_length=50,validators=[validate_name])
    nick_name    =models.CharField(max_length=50,unique=True)
    password     =models.CharField(max_length=500,validators=[validate_password])
    email        =models.EmailField(max_length=25,validators=[validate_email])
    phone_number =models.CharField(max_length=20,validators=[validate_phone_number])

    
    class Meta:
        db_table='users'
    
    
       
            



