import re

from django.core.exceptions import ValidationError


def validate_email(email):
    
    REGEX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9-.]+$'
    
    if not re.match(REGEX_EMAIL,email) :
        raise ValidationError(message='')
  
    
def validate_password(password):
    
    REGEX_PASSWORD   = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{6,25}$'
    
    if not re.match(REGEX_PASSWORD,password):
        raise ValidationError(message="INVALID_PASSWORD")
    
def validate_name(name):
    
    REGEX_NAME         ='^[a-zA-Z가-힣]+$'
    
    if not re.match(REGEX_NAME,name):
        raise ValidationError(message="INVALID_NAME")
  
def validate_phone_number(phone_number):
    
    REGEX_PHONE_NUMBER = '\d{3}-\d{4}-\d{4}'
    
    if not re.match(REGEX_PHONE_NUMBER,phone_number):
        raise ValidationError(message="INVALID_PHONE_NUMBER")


    
    
    


