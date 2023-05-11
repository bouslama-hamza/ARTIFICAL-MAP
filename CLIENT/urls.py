from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm

urlpatterns = [
    path('signup/' , views.client_signup , name='client_signup'),
    path('login/' , LoginView.as_view(
                        authentication_form = UserLoginForm , 
                        template_name='HomePages/Client Login/client_login.html',
                        ) , 
                    name='client-login'
                    ),
    path('' , views.client_home , name='client_home'),
    path('contact/' , views.client_contact , name='client_contact'),
    path('guid/' , views.client_guid , name='client_guid'),
    path('map/' , views.client_map , name='client_map'),
    path('graph/' , views.client_graph , name='client-graph'),
    path('geo/' , views.client_geo , name='client-geo'),
]