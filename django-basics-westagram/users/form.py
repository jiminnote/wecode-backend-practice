from django.forms import ModelForm
from .models import *
from validation import *

class UserForm(ModelForm):
    
    
    class Meta:
        model=User
        fields = '__all__'
        
