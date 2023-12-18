from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price =models.IntegerField(default=0)
    cost = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='Product')


    def __str__(self):
        return self.title





