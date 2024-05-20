from django.shortcuts import render, redirect
from django.views import View
from rest_framework.viewsets import ModelViewSet
from .models import Person, Cheffs
from .serializer import PersonSerializer, CheffsSerializer
from django.contrib.auth.models import User

class LoginView(View):

    def get(self, request):
        return render(request, 'form/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username, password=password)
        if user:
            print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<LOGIN>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            return redirect('register')
        else:
            print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ERROR>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            return redirect('login')




class RegisterView(View):
    def get(self, request):
        return render(request, 'form/register.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email_or_phone']
        password = request.POST['password']

        user = User(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password)
        user.save()

        return redirect('/login')


class PersonApiViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CheffsApiViewSet(ModelViewSet):
    queryset = Cheffs.objects.all()
    serializer_class = CheffsSerializer



