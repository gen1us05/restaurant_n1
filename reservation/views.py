from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import TableType, Table, BookTable
from .serializer import TableTypeSerializer, TableSerializer, BookTableSerializer



class TableTypeViewSet(ModelViewSet):
    queryset = TableType.objects.all()
    serializer_class = TableTypeSerializer

class TableViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class BookTableViewSet(ModelViewSet):
    queryset = BookTable.objects.all()
    serializer_class = BookTableSerializer


