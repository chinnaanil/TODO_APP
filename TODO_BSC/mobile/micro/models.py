from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todo(models.Model):
    task=models.TextField()
    status=models.CharField( max_length=50,default="NOT STARTED")
    due=models.DateField( auto_now=False, auto_now_add=False)
    uid=models.ForeignKey( User, on_delete=models.CASCADE)
    
    
