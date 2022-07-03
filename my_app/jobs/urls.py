from django.urls import path
from jobs import views


urlpatterns = [
    path('', views.show_jobs),
    path('single', views.show_single_job),
    path('categories', views.show_job_by_category),
    path('search', views.show_searched_jobs),
]
