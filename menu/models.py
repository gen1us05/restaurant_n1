from django.db import models



class FoodsType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Foods(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(FoodsType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='foods/')
    price = models.FloatField()
    used_products = models.ForeignKey(Product, on_delete=models.CASCADE)
    delivery = models.BooleanField(default=False)

