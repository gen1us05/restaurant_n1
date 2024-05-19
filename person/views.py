from django.shortcuts import render
from django.views import View
from rest_framework.viewsets import ModelViewSet
from .models import Person
from .serializer import PersonSerializer


class LoginView(View):

    def get(self, request):
        return render(request, 'form/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'form/register.html')


class PersonApiViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer





