from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.client_home , name='client_home'),
    path('contact/' , views.client_contact , name='client_contact'),
    path('guid/' , views.client_guid , name='client_guid'),
    path('map/' , views.client_map , name='client_map'),
]