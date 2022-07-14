from django.urls import path
from accounts import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('register_user', views.register_user, name='register_user'),
    path('user_login', views.user_login, name='user_login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
]

'''
1. define a function in views.py to return data, render page, process data etc.
2. define URL for that function in relevant module
3. call the URL in required place
'''
