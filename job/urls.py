from django.urls import path
from job import views

urlpatterns = [
    path('', views.jobs_list, name="jobs_list"),
]