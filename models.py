from django.db import models 
# Create your models here. And Class 
  

class User(models.Model):
    nm=models.CharField(max_length=50)
    em=models.CharField(max_length=50) 
    ph=models.BigIntegerField()
    dg=models.CharField(max_length=50)
    dp=models.CharField(max_length=50)
    ofid=models.BigIntegerField()
    pas=models.BigIntegerField()
   

    def __str__(self):
        return self.name







