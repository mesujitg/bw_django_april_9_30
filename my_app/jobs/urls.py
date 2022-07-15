from django.urls import path
from jobs import views


urlpatterns = [
    path('', views.show_jobs, name='jobs'),
    path('single/<id>', views.show_single_job, name='single_job'),
    path('categories/<cid>', views.show_job_by_category, name='categorized_jobs'),
    path('search', views.show_searched_jobs, name='search'),
]
