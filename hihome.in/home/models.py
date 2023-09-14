# from typing_extensions import Required
from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=100,null=False)
    lastname = models.CharField(max_length=100)
    email =models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    competetions = models.CharField(max_length=30)
    zip =models.CharField(max_length=10)
    date = models.DateField()
    
    def __str__(self):
        return self.name

class Contactus(models.Model):
    contactName = models.CharField(max_length=100)
    contactEmail = models.CharField(max_length=100)
    contactMessage = models.TextField()
    def __str__(self):
        return self.contactName

class myuploadfile(models.Model):
    f_name = models.CharField(max_length=100,default="")
    myfile = models.FileField(upload_to="")
    def __str__(self) :
        return self.f_name