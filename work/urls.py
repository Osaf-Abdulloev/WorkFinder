from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_job/', views.create_job, name='create_job')
]
