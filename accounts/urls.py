from django.urls import path, include
from . import views
from django.contrib.auth.models import User, auth

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login , name="login"),
    path('register/', views.register, name='register'),
]

if User.is_authenticated:
    urlpatterns += path('logout/', views.logout, name='logout'),