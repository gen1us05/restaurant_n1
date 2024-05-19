from rest_framework import serializers
from .models import FoodsType, Foods


class FoodsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodsType
        fields = '__all__'

class FoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = '__all__'

