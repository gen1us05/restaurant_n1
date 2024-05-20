from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=True)
    address = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='person', null=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username



class Specialitys(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Cheffs(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    speciality = models.ForeignKey(Specialitys, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, blank=True)
    address = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='cheffs', null=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name