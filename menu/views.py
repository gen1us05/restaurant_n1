from django.shortcuts import render
from django.views import View
from .models import FoodsType, Product, Foods



class LandingPageView(View):

    def get(self, request):
        foods_type = FoodsType.objects.all()
        foods = Foods.objects.all()

        context = {
            'foods_type': foods_type,
            'foods': foods
        }
        return render(request, 'index.html', context)




