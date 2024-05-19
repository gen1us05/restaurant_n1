from django.urls import path, include
from .views import LandingPageView, FoodsTypeAPIViewSet, FoodsAPIViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('foods-type', viewset=FoodsTypeAPIViewSet)
router.register('foods', viewset=FoodsAPIViewSet)

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path("", include(router.urls)),
]
