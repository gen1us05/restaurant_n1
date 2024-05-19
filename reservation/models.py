from django.db import models
from person.models import Person




class TableType(models.Model):
    name = models.CharField(max_length=25)
    price = models.SmallIntegerField()

    def __str__(self):
        return self.name

class Table(models.Model):
    table_number = models.SmallIntegerField()
    chairs_number = models.SmallIntegerField()
    table_type = models.ForeignKey(TableType, on_delete=models.CASCADE)

    def __str__(self):
        table = str(int(self.table_number))
        return table


class BookTable(models.Model):
    table_number = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    usage_time_start = models.DateTimeField(auto_created=True)
    usage_time_end = models.DateTimeField(auto_created=True)







