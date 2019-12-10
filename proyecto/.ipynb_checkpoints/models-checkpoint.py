from django.db import models

# Create your models here.

class user_model(models.Model):
    ##id = models.CharField(max_length=200)
    born_date = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
        
        
class position_model(models.Model):
   ## id=models.CharField(max_length=200)
    altitude=models.CharField(max_length=200)
    latitude=models.CharField(max_length=200)
    longitude=models.CharField(max_length=200)
    user_id=models.CharField(max_length=200)