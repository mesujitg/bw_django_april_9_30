from django.urls import path
from information import views


urlpatterns = [
    # 127.0.0.1:8000/info/about
    path('about', views.show_about, name='about'),

    # 127.0.0.1:8000/info/contacts
    path('contacts', views.show_contacts, name='contacts'),

    # 127.0.0.1:8000/info/policies
    path('policies', views.show_policies, name='policies'),
]
