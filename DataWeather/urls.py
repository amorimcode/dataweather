from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('dataweather/', include('dataweather.urls')),
    path('admin/', admin.site.urls),
]