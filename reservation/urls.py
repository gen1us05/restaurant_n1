from django.urls import path, include
from .views import TableTypeViewSet, TableViewSet, BookTableViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('table-type', viewset=TableTypeViewSet)
router.register('tables', viewset=TableViewSet)
router.register('book-table', viewset=BookTableViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
