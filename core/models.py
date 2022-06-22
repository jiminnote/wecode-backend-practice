from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Mete:
        abstract = True