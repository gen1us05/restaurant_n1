from rest_framework import serializers
from .models import TableType, Table, BookTable


class TableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableType
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class BookTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTable
        fields = '__all__'


