from django.urls import path
from applications import views


urlpatterns = [
    path('apply/<jid>', views.apply, name='apply')
]
