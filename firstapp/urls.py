from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.loginuser,name='loginuser'),
    path('logout',views.logoutuser,name='logoutuser'),
]