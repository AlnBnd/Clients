from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('client_list/', views.client_list, name='client_list'),
    path('update_client_status/<int:client_id>/', views.update_client_status, name='update_client_status'),
]