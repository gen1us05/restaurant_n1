from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()           #keyinchalik sms keladigon qlinadi
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='person')

    def __str__(self):
        return self.first_name

