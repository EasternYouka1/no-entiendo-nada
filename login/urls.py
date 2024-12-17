from django.urls import path, include
from .views import home, landing, login_view, register_view,logout_view

urlpatterns = [
    path("", landing, name="landing"),
    path('login/', login_view, name='login'),
    path("home/", home, name="home"),  
    path('register/', register_view, name='register'),
    
]