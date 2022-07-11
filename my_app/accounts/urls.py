from django.urls import path
from accounts import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('register_user', views.register_user, name='register_user'),
]
