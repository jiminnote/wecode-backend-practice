
from collections import UserString
from django.db import models


class TimeStampModel(models.Model):
    create_at=models.DateTimeField(aauto_now_add=True)
    update_at=models.DateTimeField(aauto_now=True)
    
    class Meta:
        abstract = True
    
class Post(TimeStampModel):
    users=models.ForeignKey("users.User",on_delete=models.CASCADE)
    img_urls=models.URLField()
    posts=models.TextField()
    
    class Meta:
        db_table='posts'
    

    
