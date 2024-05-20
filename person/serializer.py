from rest_framework import serializers
from .models import Person, Cheffs


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class CheffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheffs
        fields = '__all__'



