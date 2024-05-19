from django.shortcuts import render
from django.views import View
from rest_framework.viewsets import ModelViewSet
from .models import FoodsType, Foods
from .serializer import FoodsTypeSerializer, FoodsSerializer




class LandingPageView(View):

    def get(self, request):
        foods_type = FoodsType.objects.all()
        foods = Foods.objects.all()

        context = {
            'foods_type': foods_type,
            'foods': foods
        }
        return render(request, 'index.html', context)



class FoodsTypeAPIViewSet(ModelViewSet):
    queryset = FoodsType.objects.all()
    serializer_class = FoodsTypeSerializer



class FoodsAPIViewSet(ModelViewSet):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializer

