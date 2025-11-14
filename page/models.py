from django.db import models

# Create your models here.
class list(models.Model):
    img=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=25)
    heading=models.CharField(max_length=25,default='pop') 


class delights(models.Model):
    img=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=50)
    price=models.IntegerField()

class popsicles(models.Model):
    img=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=50)
    price=models.IntegerField()

class cheese(models.Model):
    img=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=50)
    price=models.IntegerField()

class ice_library(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Product(models.Model):
    pid=models.IntegerField()
    cid=models.ForeignKey(ice_library,on_delete=models.CASCADE,blank=False,related_name='product')
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    badge=models.TextField()
    rating=models.IntegerField()
    price=models.IntegerField()
    

    

    def __str__(self):
        return self.name
