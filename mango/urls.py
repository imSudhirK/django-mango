from django.contrib import admin
from django.urls import path
from mango import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('dashboard', views.dashboard, name="Dashboard"),
    path('about', views.about, name="About"),
    path('services', views.services, name="Services"),
    path('contact', views.contact, name="Contact"),
    path('register-user', views.registerUser, name="Register User"),
    path('login-user', views.loginUser, name="Login User"),
    path('logout-user', views.logoutUser, name="Logout User")
]