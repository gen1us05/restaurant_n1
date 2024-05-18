from django.db import models
from person.models import Person




class TableType(models.Model):
    name = models.CharField(max_length=25)
    price = models.SmallIntegerField()

    def __init__(self):
        return self.name


class Table(models.Model):
    table_number = models.SmallIntegerField()
    chairs_number = models.SmallIntegerField()
    table_type = models.ForeignKey(TableType, on_delete=models.CASCADE)

    def __init__(self):
        return self.table_number


class BookTable(models.Model):
    booking_number = models.SmallIntegerField()
    table_number = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    usage_time_start = models.DateTimeField(auto_created=True)
    usage_time_end = models.DateTimeField(auto_created=True)

    def __init__(self):
        return self.booking_number






