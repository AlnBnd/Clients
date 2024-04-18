from django.contrib import admin
from django.urls import path, include
# from data.views import client_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('data.urls')),
]
