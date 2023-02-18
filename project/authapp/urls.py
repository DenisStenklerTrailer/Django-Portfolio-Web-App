from django.contrib import admin
from django.urls import path
from .views import signup,handleLogin,handleLogout

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', handleLogin, name='handleLogin'),
    path('logout/', handleLogout, name='handleLogout'),
]
