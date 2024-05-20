from django.urls import path, include
from .views import LoginView, RegisterView, PersonApiViewSet, CheffsApiViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('person', viewset=PersonApiViewSet)
router.register('cheffs', viewset=CheffsApiViewSet)


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('api/', include(router.urls)),
]
