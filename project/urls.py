from django.contrib import admin
from django.urls import path, include
from api.urls import urlpatterns

urlpatterns = [
    path('', include(urlpatterns)),
    path('admin/', admin.site.urls),
]

