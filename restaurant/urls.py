from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('person.urls')),
    path('', include('menu.urls')),
    path('', include('reservation.urls')),
    path('api/v1/', include("menu.urls")),
    path('api/v1/', include("person.urls")),
    path('api/v1/', include("reservation.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
